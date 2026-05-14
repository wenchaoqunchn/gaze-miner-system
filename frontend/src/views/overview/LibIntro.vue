<template>
    <div class="main-content">
        <div class="aoi breadcrumb" data-aoi-type="info" data-aoi-desc="面包屑位置提示" data-aoi-group="lib-intro">
            您当前所在位置 ： 首页 > 图书馆概况 > 本馆介绍
        </div>
        <div class="aoi title" data-aoi-type="info" data-aoi-desc="页面主标题-本馆介绍" data-aoi-group="lib-intro">
            <h2>本馆介绍</h2>
        </div>
        <div class="aoi content" data-aoi-type="info" data-aoi-desc="本馆介绍正文：包含建馆历史、总面积、馆藏数据及机构合作"
            data-aoi-group="lib-intro">
            <img src="../../assets/libintro.jpg" alt="图书馆" class="float-image" />
            <p>北京工业大学图书馆始建于1960年，馆舍几经变迁，目前可供使用的有2处，分别位于校本部及通州校区。校本部图书馆于2019年9月启用，面积4万余平米，座位数3000余个；通州校区图书馆面积两千余平米，座位数500余个。图书馆实行藏、借、阅一体的开放式服务模式，每周开馆105小时。图书馆现有职工60余人，具有硕士以上学位的职工占三分之一以上。
            </p>
            <p>目前，我馆收藏中外文纸质图书两百万余册，中外文期刊杂志一千六百多种，并拥有丰富的电子资源，形成了以工科为主，理、工、文等多种学科兼有，纸本、电子、多媒体等多种类型的文献资源体系，基本上满足了学校的教学、科研的需求。
            </p>
            <p>图书馆除了传统的图书借阅服务以外，目前还提供科技查新、文献传递、馆际互借、查收录引用、文献检索课教学、学科情报分析、知识产权信息服务，上网、自助借还等服务。</p>
            <p>北京工业大学图书馆与国家图书馆、首都图书馆、中科院文献情报中心等多家单位建立了文献信息资源的共知、共建和共享的合作关系；加入了OCLC、CALIS和BALIS等馆际合作网络，在数据库集团采购、联机合作编目、教学参考书全文库建设、联合参考咨询和馆际互借与文献传递等方面全面合作；作为CALIS市属市管高校文献信息中心和BALIS馆际互借中心，为北京地区的高校图书馆提供馆际互借的管理与服务。
            </p>
            <p>目前，我馆正在加强现代化的网络与应用系统建设。图书馆拥有存储容量近百T的磁盘阵列及多种型号服务器，不仅向读者提供书目检索、信息查询等服务，还为广大教师和学生提供网络远程服务。所有电子文献资源全天候24小时开放。
            </p>
        </div>
    </div>
</template>
<script setup>
</script>

<style scoped>
.title {
    text-align: center;
}

.main-box {
    background-color: rgba(255, 255, 255, 0.928);
    height: 95%;
    padding: 20px 200px;
    text-align: left;
    display: flex;
}

.sidebar {
    flex: 1;
}

.bar-title {
    background-size: cover;
    background-position: center;
    background-image: url(../assets/sidebar.png);
    text-align: center;
}

.main-content {
    flex: 3;
    padding: 0 5%;
}

.content {
    text-indent: 2em;
    font-size: 18px;
    line-height: 1.8;
}

.float-image {
    float: right;
    /* 使图片浮动到右侧 */
    margin-left: 20px;
    /* 图片与文本之间的间距 */
    margin-bottom: 10px;
    /* 图片下方与文本之间的间距 */
    max-width: 350px;
    /* 设置图片的最大宽度 */
    height: auto;
    /* 自适应高度 */
}
</style>