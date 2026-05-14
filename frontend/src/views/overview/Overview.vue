<template>
    <div class="main-box">
        <div class="sidebar">
            <div class="bar-title">
                <h2 class="aoi" data-aoi-type="info" data-aoi-desc="侧边栏主标题-图书馆概况" data-aoi-group="overview-sidebar">
                    图书馆概况
                </h2>
            </div>
            <el-menu :default-active="activeMenu" class="el-menu-vertical" @select="handleSelect"
                background-color="#f7f7f7" text-color="#333" active-text-color="#20a0ff" mode="vertical">
                <el-menu-item class="aoip" index="LibIntro" data-aoi-type="nav" data-aoi-desc="导航至本馆介绍页"
                    data-aoi-group="overview-menu">本馆介绍</el-menu-item>
                <el-menu-item class="aoip" index="LeaderSpeech" data-aoi-type="nav" data-aoi-desc="导航至馆长致辞页"
                    data-aoi-group="overview-menu">馆长致辞</el-menu-item>
                <el-menu-item class="aoip" index="LibRule" data-aoi-type="nav" data-aoi-desc="导航至规章制度页"
                    data-aoi-group="overview-menu">规章制度</el-menu-item>
                <el-menu-item class="aoip" index="ServiceTime" data-aoi-type="nav" data-aoi-desc="导航至服务时间页"
                    data-aoi-group="overview-menu">服务时间</el-menu-item>
                <el-menu-item class="aoip" index="ServiceOverview" data-aoi-type="nav" data-aoi-desc="导航至服务一览页"
                    data-aoi-group="overview-menu">服务一览</el-menu-item>
                <el-menu-item class="aoip" index="LibLayout" data-aoi-type="nav" data-aoi-desc="导航至图书馆布局页"
                    data-aoi-group="overview-menu">图书馆布局</el-menu-item>
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

// 根据当前路由名称初始化 activeMenu
const activeMenu = ref(route.name);
// 处理菜单选择
const handleSelect = (index) => {
    activeMenu.value = index; // 更新当前选中的菜单项
    router.push({ name: index }); // 路由跳转到对应的内容
};

// 监视路由变化，更新 activeMenu
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