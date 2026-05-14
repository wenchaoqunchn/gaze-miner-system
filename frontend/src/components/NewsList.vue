<template>
    <div class="news-container">
        <h1 class="aoi header" data-aoi-type="info" data-aoi-desc="最新资讯模块主标题" data-aoi-group="news-list">最新资讯</h1>

        <el-table class="aoi tab" :data="newsList" data-aoi-type="info" data-aoi-desc="最新资讯动态列表(含讲座通知、资源推荐等详细条目)"
            data-aoi-group="news-list">
            <el-table-column prop="date" label="发布日期" width="80">
                <template #default="{ row }">
                    <span class="date">{{ row.date }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="type" label="资讯类型" width="100">
                <template #default="{ row }">
                    <span :class="['type', getTypeClass(row.type)]">{{ row.type }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="title" label="资讯内容">
                <template #default="{ row }">
                    <span class="title">{{ row.title }}</span>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    name: 'NewsList',
    data() {
        return {
            newsList: [
                { date: '10-24', type: '讲座通知', title: '“科研智汇·情报赋能”系列讲座' },
                { date: '09-27', type: '通知公告', title: '首届在京高校知识产权信息检索大赛(专利检索技能竞赛)9月28日开启' },
                { date: '09-27', type: '通知公告', title: '关于2024级学术学位研究生《科技文献检索与利用》 课程开课的通知' },
                { date: '09-24', type: '资源推荐', title: '最新版《中国科技核心期刊目录》（2024年版）已发布' },
                { date: '09-24', type: '资源试用', title: 'Small Methods 、Advanced Energy Materials 等70种Wiley期刊开通试用' },
                { date: '09-23', type: '通知公告', title: '首届在京高校知识产权信息检索大赛：技能竞赛赛前培训' },
            ],
        };
    },
    methods: {
        getTypeClass(type) {
            switch (type) {
                case '讲座通知':
                    return 'lecture';
                case '通知公告':
                    return 'announcement';
                case '资源推荐':
                    return 'resource-recommendation';
                case '资源试用':
                    return 'resource-trial';
                default:
                    return '';
            }
        },
    },
};
</script>

<style scoped>
.news-container {
    padding: 20px;
}

.header {
    font-size: 36px;
    margin: 0;
}

.tab {
    background-color: white;
}

.date,
.title {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.type {
    display: inline-block;
    border-radius: 50px;
    padding: 0px 15px;
    /* 左右padding */
    color: white;
    font-size: 10px;
    /* 字体颜色 */
}

.lecture {
    background-color: rgb(30, 173, 198);
}

.announcement {
    background-color: rgb(241, 154, 5);
}

.resource-recommendation {
    background-color: rgb(88, 191, 19);
}

.resource-trial {
    background-color: rgb(85, 144, 233);
}
</style>