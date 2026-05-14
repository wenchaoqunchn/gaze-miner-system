
function getAOIInfo(viewName = 'View') {
    const elements = document.querySelectorAll('.aoim, .aoip, .aoi, .key-aoi');
    const info = [];

    elements.forEach((element, index) => {
        const rect = element.getBoundingClientRect();
        const computedStyle = window.getComputedStyle(element);
        const dataset = element.dataset;

        // 1. 保留旧版的 margin/padding 坐标微调逻辑
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

        // 2. 保留旧版的 1.5倍缩放 和 124px 偏移逻辑
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

        const isKeyAOI = element.classList.contains('key-aoi');
        const componentInfo = element.className;

        // 3. 构建大模型专属的唯一学术 ID
        const aoiId = `${viewName}_${index + 1}`;

        // 4. 组装数据并 push（兼容旧字段 + 增加新字段）
        info.push({
            // === 兼容旧系统必需字段（绝对不能删）===
            topLeft: finalTopLeft,
            bottomRight: finalBottomRight,
            isKeyAOI: isKeyAOI,
            componentInfo: componentInfo,

            // === GazeReasoner 升维新增的 VLM 专属字段 ===
            id: aoiId,
            mark_number: index + 1, // 用于 SOM 标注对齐的唯一数字
            width: Math.round((innerBottomRight.x - innerTopLeft.x) * scale),
            height: Math.round((innerBottomRight.y - innerTopLeft.y) * scale),

            // 业务语义维度 (从刚才你在 HTML 里加的 data-* 提取)
            semantics: {
                type: dataset.aoiType || "unknown",
                description: dataset.aoiDesc || "",
                group: dataset.aoiGroup || "global",
                tagName: element.tagName.toLowerCase()
            },

            // 交互状态维度
            state: {
                is_disabled: element.disabled || element.hasAttribute('disabled') || element.classList.contains('is-disabled'),
                is_visible: computedStyle.display !== 'none' && computedStyle.visibility !== 'hidden',
                innerText: (element.innerText || "").substring(0, 100).trim(),
            },

            // 源码切片维度
            html_snippet: element.outerHTML.substring(0, 500)
        });
    });

    return info;
}
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