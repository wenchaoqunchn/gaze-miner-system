<template>
    <div class="main-content">
        <div class="aoi breadcrumb" data-aoi-type="info" data-aoi-desc="面包屑位置提示" data-aoi-group="service-time">
            您当前所在位置 ： 首页 > 图书馆概况 > 服务时间
        </div>
        <div class="aoi title" data-aoi-type="info" data-aoi-desc="页面主标题-服务时间" data-aoi-group="service-time">
            <h2>服务时间</h2>
        </div>
        <div class="aoi content" data-aoi-type="info" data-aoi-desc="服务时间表格：详细列出各阅览区、书库的开放和闭馆时间"
            data-aoi-group="service-time">
            <table class="service-table">
                <thead>
                    <tr>
                        <th>区域</th>
                        <th>服务项目</th>
                        <th>开馆时间</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan="6">主校区</td>
                        <td>阅览区</td>
                        <td>周一至周日 7：30～22：30</td>
                    </tr>
                    <tr>
                        <td>人工借还书</td>
                        <td>周一至周五 8：00～21：00<br>周六、周日 8：30～11：30；13：30～16：30</td>
                    </tr>
                    <tr>
                        <td>密集书库</td>
                        <td>周一至周日 8：00～17：00</td>
                    </tr>
                    <tr>
                        <td>自修室</td>
                        <td>周一至周日 7：00～23:00（考试期间请关注临时通知）</td>
                    </tr>
                    <tr>
                        <td>研讨室</td>
                        <td>周一至周日 8：00～21：00</td>
                    </tr>
                    <tr>
                        <td>影音室</td>
                        <td>周一至周日 8：00～22：00</td>
                    </tr>
                    <tr>
                        <td>中蓝公寓</td>
                        <td colspan="2">8：00～23：00</td>
                    </tr>
                </tbody>
            </table>

            <p>备注：</p>
            <ol>
                <li>开馆时间内主校区提供自助借还服务；</li>
                <li>国家法定假日期间闭馆。</li>
            </ol>
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