<template>
    <div class="main-box">
        <div class="sidebar">
            <div class="bar-title">
                <h2 class="aoi" data-aoi-type="info" data-aoi-desc="侧边栏主标题-资源导航" data-aoi-group="resources-sidebar">
                    资源
                </h2>
            </div>
            <el-menu :default-active="activeMenu" class="el-menu-vertical" @select="handleSelect"
                background-color="#f7f7f7" text-color="#333" active-text-color="#20a0ff" mode="vertical">
                <el-menu-item class="aoip" index="CoreJournal" data-aoi-type="nav" data-aoi-desc="导航至核心期刊导航页"
                    data-aoi-group="resources-menu">核心期刊导航</el-menu-item>
                <el-menu-item class="aoip" index="EBook" data-aoi-type="nav" data-aoi-desc="导航至电子图书页"
                    data-aoi-group="resources-menu">电子图书</el-menu-item>
                <el-menu-item class="aoip" index="LibThesis" data-aoi-type="nav" data-aoi-desc="导航至学位论文页"
                    data-aoi-group="resources-menu">学位论文</el-menu-item>
                <el-menu-item class="aoip" index="CommonApp" data-aoi-type="nav" data-aoi-desc="导航至常用工具软件页"
                    data-aoi-group="resources-menu">常用工具软件</el-menu-item>
                <el-menu-item class="aoip" index="Copyright" data-aoi-type="nav" data-aoi-desc="导航至版权公告页"
                    data-aoi-group="resources-menu">版权公告</el-menu-item>
            </el-menu>
        </div>
        <div class="main-content">
            <router-view></router-view>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
const router = useRouter();
const route = useRoute();
const activeMenu = ref(route.name); // 默认选中的菜单项


const handleSelect = (index) => {
    activeMenu.value = index; // 更新当前选中的菜单项
    router.push({ name: index }); // 路由跳转到对应的内容
};
watch(() => route.name, (newName) => {
    activeMenu.value = newName;
});
</script>

<style scoped>
h2 {
    margin: 0;
}

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
    border: 1px solid #ccc;
    height: fit-content;
}

.bar-title {
    padding: 20px 0;
    background-size: cover;
    background-position: center;
    background-image: url(../../assets/sidebar.png);
    text-align: center;
}

.main-content {
    flex: 3;
    padding: 0 5%;
}

.content {
    line-height: 1;
}

table {
    line-height: 0.5;
}

.el-menu-item {
    font-size: 18px;
    /* 设置字体大小 */
}
</style>