<template>
    <div class="main-content">
        <div class="aoi breadcrumb" data-aoi-type="info" data-aoi-desc="面包屑位置提示" data-aoi-group="e-book">
            您当前所在位置 ： 首页 > 资源 > 电子图书
        </div>
        <div class="aoi title" data-aoi-type="info" data-aoi-desc="页面主标题-电子图书" data-aoi-group="e-book">
            <h2>电子图书</h2>
        </div>
        <div class="aoi content" data-aoi-type="info" data-aoi-desc="已购中外文电子图书资源列表与馆际互借说明" data-aoi-group="e-book">
            <h3>一. 已购中外文电子图书</h3>
            <table>
                <thead>
                    <tr>
                        <th>资源名称</th>
                        <th>说明</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>超星电子图书（中文）</td>
                        <td>涵盖多学科电子图书百万余种</td>
                    </tr>
                    <tr>
                        <td>Springer电子图书（外文）</td>
                        <td>我校有使用权（2008-2020版权年）的外文电子图书，及2004年以前的计算机、数学、物理学类回溯电子丛书</td>
                    </tr>
                    <tr>
                        <td>Ebsco电子图书（外文）</td>
                        <td>涵盖多学科外文电子图书9千多种</td>
                    </tr>
                    <tr>
                        <td>WeL电子图书（外文）</td>
                        <td>涵盖人文社会科学为主的多学科电子图书及有声读物</td>
                    </tr>
                    <tr>
                        <td>Wiley参考工具书（外文）</td>
                        <td>28种wiley参考工具书</td>
                    </tr>
                </tbody>
            </table>

            <h3>二. 文献传递与馆际互借</h3>
            <p>我馆未购买的图书可通过文献传递与馆际互借服务获取。</p>
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

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th,
td {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f7f7f7;
}
</style>