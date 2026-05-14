
/**
 * 提取当前页面中所有 AOI（Area of Interest，兴趣区）元素的屏幕空间信息，并输出结构化 JSON。
 *
 * ### 设计目标
 * 1) **兼容旧系统**：保留历史版本中依赖的字段与坐标变换（margin/padding 微调、1.5 缩放、124px 偏移）。
 * 2) **面向多模态分析**：为后续 VLM/LLM（如 GazeReasoner）增加语义/状态/源码片段等信息，做到“坐标 + 语义”统一。
 * 3) **可复用**：作为纯函数返回数据，调用方可选择写入 Vuex、上传后端或下载文件。
 *
 * ### AOI 选择规则
 * 默认搜集以下 class 的元素：
 * - `.aoi`  : 普通兴趣区
 * - `.aoim` : margin 对齐型兴趣区（会把 margin 计入区域）
 * - `.aoip` : padding 对齐型兴趣区（会扣除 padding 取 content-box）
 * - `.key-aoi` : 关键兴趣区（如关键按钮、流程关键节点等）
 *
 * ### 坐标系说明
 * - `getBoundingClientRect()` 返回的是**浏览器视口坐标**（CSS 像素），与屏幕截图的像素坐标可能不一致。
 * - 目前项目沿用旧版逻辑：对 AOI 坐标做 `scale=1.5` 的缩放，并对 y 加上 `topOffset=124`。
 *   这通常用于把网页内坐标映射到“实验采集截图/显示器坐标系”。
 *   若未来屏幕分辨率、缩放比例或浏览器 UI 高度变化，应将这些参数从硬编码改为可配置项。
 *
 * @param {string} viewName - 页面名/视图名，用于构建 AOI 的全局唯一 id（通常传入路由 name）。
 * @returns {Array<Object>} AOI 信息数组。每个对象同时包含旧字段与新增字段。
 */
function getAOIInfo(viewName = 'View') {
    // 选择所有 AOI 元素（按 class 约定进行统一收集）
    const elements = document.querySelectorAll('.aoim, .aoip, .aoi, .key-aoi');
    const info = [];

    elements.forEach((element, index) => {
        // DOMRect：相对浏览器 viewport 的可见区域坐标（CSS 像素单位）
        const rect = element.getBoundingClientRect();
        // 计算样式：用于读取 margin/padding、display/visibility 等影响区域与可见性的属性
        const computedStyle = window.getComputedStyle(element);
        // dataset：从 HTML 的 data-aoi-* 中提取业务语义（会自动把 data-aoi-type 转成 aoiType）
        const dataset = element.dataset;

        // ------------------------------------------------------------------
        // 1) 旧版：margin/padding 坐标微调逻辑
        // ------------------------------------------------------------------
        // innerTopLeft/innerBottomRight 表示“调整后的内容区域”坐标。
        // - 默认直接取 bounding rect（border-box 区域）
        // - aoim：把 margin 也纳入兴趣区（向外扩）
        // - aoip：扣除 padding，尽量贴近 content-box（向内收）
        let innerTopLeft = { x: rect.left, y: rect.top };
        let innerBottomRight = { x: rect.right, y: rect.bottom };

        if (element.classList.contains('aoim')) {
            const marginLeft = parseFloat(computedStyle.marginLeft) || 0;
            const marginTop = parseFloat(computedStyle.marginTop) || 0;
            innerTopLeft.x -= marginLeft;
            innerTopLeft.y -= marginTop;
            innerBottomRight.x += parseFloat(computedStyle.marginRight) || 0;
            innerBottomRight.y += parseFloat(computedStyle.marginBottom) || 0;
        } else if (element.classList.contains('aoip')) {
            const paddingLeft = parseFloat(computedStyle.paddingLeft) || 0;
            const paddingTop = parseFloat(computedStyle.paddingTop) || 0;
            innerTopLeft.x += paddingLeft;
            innerTopLeft.y += paddingTop;
            innerBottomRight.x -= parseFloat(computedStyle.paddingRight) || 0;
            innerBottomRight.y -= parseFloat(computedStyle.paddingBottom) || 0;
        }

        // ------------------------------------------------------------------
        // 2) 旧版：坐标映射（scale + topOffset）
        // ------------------------------------------------------------------
        // 说明：该变换来自历史实验环境（例如屏幕缩放、窗口位置或上边栏高度）。
        // 注意：这不是标准做法，但为了兼容“截图像素坐标系”与“页面坐标系”的对齐，先保留。
        const scale = 1.5;
        const topOffset = 124;

        let finalTopLeft = {
            x: Math.round(innerTopLeft.x * scale),
            y: Math.round(innerTopLeft.y * scale + topOffset)
        };
        let finalBottomRight = {
            x: Math.round(innerBottomRight.x * scale),
            y: Math.round(innerBottomRight.y * scale + topOffset)
        };

        // key-aoi 标记关键兴趣区，在分析/报告中可能给予更高权重
        const isKeyAOI = element.classList.contains('key-aoi');
        // 兼容旧字段：使用 className 做组件信息（旧版可能以此判断组件类型）
        const componentInfo = element.className;

        // ------------------------------------------------------------------
        // 3) 新增：构建唯一 ID（面向多模态/大模型）
        // ------------------------------------------------------------------
        // 用 viewName + 序号拼接生成稳定 id。
        // 约束：在同一次采集中，同一个 viewName 下 index 顺序稳定即可。
        const aoiId = `${viewName}_${index + 1}`;

        // ------------------------------------------------------------------
        // 4) 组装 AOI 数据（旧字段 + 新字段）
        // ------------------------------------------------------------------
        info.push({
            // === 兼容旧系统必需字段（绝对不能删）===
            topLeft: finalTopLeft,
            bottomRight: finalBottomRight,
            isKeyAOI: isKeyAOI,
            componentInfo: componentInfo,

            // === GazeReasoner 升维新增的 VLM 专属字段 ===
            id: aoiId,
            mark_number: index + 1, // 用于 SOM 标注对齐的唯一数字
            // width/height：以“映射后的坐标系”为准的 AOI 宽高，方便画框或做裁剪
            width: Math.round((innerBottomRight.x - innerTopLeft.x) * scale),
            height: Math.round((innerBottomRight.y - innerTopLeft.y) * scale),

            // 业务语义维度（推荐在组件上声明 data-aoi-* 来提高可解释性）
            // - type：AOI 类型（nav/action/input/info...）
            // - description：自然语言描述
            // - group：逻辑分组（用于同模块聚合分析）
            semantics: {
                type: dataset.aoiType || "unknown",
                description: dataset.aoiDesc || "",
                group: dataset.aoiGroup || "global",
                tagName: element.tagName.toLowerCase()
            },

            // 交互状态维度（帮助判断：用户是否在看一个不可点击/不可见元素）
            state: {
                is_disabled: element.disabled || element.hasAttribute('disabled') || element.classList.contains('is-disabled'),
                is_visible: computedStyle.display !== 'none' && computedStyle.visibility !== 'hidden',
                // innerText 仅截取前 100 字，避免表格/长文本导致 JSON 过大
                innerText: (element.innerText || "").substring(0, 100).trim(),
            },

            // 源码切片维度：用于 debug 或做弱监督（同样截断避免体积爆炸）
            html_snippet: element.outerHTML.substring(0, 500)
        });
    });

    return info;
}
// ----------------------------------------------------------------------
// 下载工具：将 JSON 作为文件下载
// ----------------------------------------------------------------------
// 注意：此方法只负责“下载”，不负责“采集”。采集请调用 getAOIInfo。
// 本方法保留为工具函数，方便在 SessionDone 或调试时快速导出。
// ------ 保持旧版下载函数的名称和参数完全不变 ------
function downloadJSON(data, filename) {
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// 统一导出，保证各种老代码调用都不报错
export { getAOIInfo, downloadJSON };