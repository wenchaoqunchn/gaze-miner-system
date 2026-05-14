<template>
    <div class="main-content">
        <div class="aoi breadcrumb" data-aoi-type="info" data-aoi-desc="面包屑位置提示" data-aoi-group="service-overview">
            您当前所在位置 ： 首页 > 图书馆概况 > 服务一览
        </div>
        <div class="aoi title" data-aoi-type="info" data-aoi-desc="页面主标题-服务一览" data-aoi-group="service-overview">
            <h2>服务一览</h2>
        </div>
        <div class="aoi content" data-aoi-type="info" data-aoi-desc="服务一览表格：列出科技查新、座位预约等各项服务的内容、地点与咨询电话"
            data-aoi-group="service-overview">
            <table class="service-table">
                <thead>
                    <tr>
                        <th>服务项目</th>
                        <th>服务地点</th>
                        <th>咨询电话</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>B-报刊阅览</td>
                        <td>图书馆三层期刊阅览区<br></td>
                        <td>010-67391819<br></td>
                    </tr>
                    <tr>
                        <td>G-馆际互借与文献传递</td>
                        <td>图书馆二层总服务台（还书、取书地点）</td>
                        <td>010-67396518</td>
                    </tr>
                    <tr>
                        <td>K-科技查新</td>
                        <td>图书馆二层咨询部2室（236房间）</td>
                        <td>010-67396687</td>
                    </tr>
                    <tr>
                        <td>L-查论文收录及引用</td>
                        <td>图书馆一层咨询部1室（129房间）</td>
                        <td>010-67392185</td>
                    </tr>
                    <tr>
                        <td>S-随书光盘借阅</td>
                        <td>图书馆二层总服务台</td>
                        <td>010-67391819</td>
                    </tr>
                    <tr>
                        <td>T-图书借阅</td>
                        <td>图书馆二层总服务台</td>
                        <td>010-67391819</td>
                    </tr>
                    <tr>
                        <td>X-学科信息服务</td>
                        <td>图书馆一层咨询部1室（129房间）</td>
                        <td>010-67392185</td>
                    </tr>
                    <tr>
                        <td>X-学位论文提交</td>
                        <td>图书馆五层技术部</td>
                        <td>010-67391816</td>
                    </tr>
                    <tr>
                        <td>Y-研讨室预约</td>
                        <td>图书馆二层服务台</td>
                        <td>010-67396501</td>
                    </tr>
                    <tr>
                        <td>Z-知识产权信息服务</td>
                        <td>图书馆一层咨询部1室（129房间）</td>
                        <td>010-67392185</td>
                    </tr>
                    <tr>
                        <td>Z-证件办理及挂失补</td>
                        <td>图书馆二层总服务台</td>
                        <td>010-67391819</td>
                    </tr>
                    <tr>
                        <td>Z-座位预约</td>
                        <td>线上预约时间：07:00－22:00</td>
                        <td>010-67391819</td>
                    </tr>
                </tbody>
            </table>
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
    font-size: 18px;
    line-height: 1.6;
}

.service-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

.service-table th,
.service-table td {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: left;
}

.service-table th {
    background-color: #f2f2f2;
}
</style>