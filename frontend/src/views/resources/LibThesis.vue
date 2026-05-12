<template>
    <div class="main-content">
        <div class="aoi breadcrumb">
            您当前所在位置 ： 首页 > 资源 > 学位论文
        </div>
        <div class="aoi title">
            <h2>北工大学位论文</h2>
        </div>
        <div class="aoi content">
            <p>北京工业大学学位论文库收录本校1997年以来公开的博士论文、1996年以来公开的硕士论文和2008年以来公开的部分优秀本科学位论文，校内用户可查阅下载全文。</p>

            <p>论文查询网址：<a href="https://libthesis.bjut.edu.cn" target="_blank">https://libthesis.bjut.edu.cn</a></p>
            <img src="../../assets/thesis.jpg" alt="北工大学位论文" class="thesis-image" />
        </div>
    </div>
</template>

<script setup>
</script>

<style scoped>
.title {
    text-align: center;
}

.main-content {
    padding: 20px 5%;
}

.content {
    text-indent: 2em;
    font-size: 18px;
    line-height: 1.6;
}

.thesis-image {
    display: block;
    /* 确保图片为块级元素，文字不环绕 */
    margin: 20px auto;
    /* 居中图片并添加上下间距 */
    max-width: 65%;
    /* 使图片响应式 */
    height: auto;
    /* 保持图片纵横比 */
}
</style>