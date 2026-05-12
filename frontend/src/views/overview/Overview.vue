<template>
    <div class="main-box">
        <div class="sidebar">
            <div class="bar-title">
                <h2 class="aoi">图书馆概况</h2>
            </div>
            <el-menu :default-active="activeMenu" class="el-menu-vertical" @select="handleSelect"
                background-color="#f7f7f7" text-color="#333" active-text-color="#20a0ff" mode="vertical">
                <el-menu-item class="aoip" index="LibIntro">本馆介绍</el-menu-item>
                <el-menu-item class="aoip" index="LeaderSpeech">馆长致辞</el-menu-item>
                <el-menu-item class="aoip" index="LibRule">规章制度</el-menu-item>
                <el-menu-item class="aoip" index="ServiceTime">服务时间</el-menu-item>
                <el-menu-item class="aoip" index="ServiceOverview">服务一览</el-menu-item>
                <el-menu-item class="aoip" index="LibLayout">图书馆布局</el-menu-item>
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