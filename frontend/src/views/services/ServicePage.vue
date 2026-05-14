<template>
    <div class="main-box">
        <div class="sidebar">
            <div class="bar-title">
                <h2 class="aoi" data-aoi-type="info" data-aoi-desc="侧边栏主标题-服务导航" data-aoi-group="service-sidebar">服务
                </h2>
            </div>
            <el-menu :default-active="activeMenu" class="el-menu-vertical" @select="handleSelect"
                background-color="#f7f7f7" text-color="#333" active-text-color="#20a0ff" mode="vertical">
                <el-menu-item class="aoip" index="BookBorrow" data-aoi-type="nav" data-aoi-desc="导航至书刊借阅页"
                    data-aoi-group="service-menu">书刊借阅</el-menu-item>
                <el-menu-item class="aoip" index="CardProcess" data-aoi-type="nav" data-aoi-desc="导航至证件办理页"
                    data-aoi-group="service-menu">证件办理</el-menu-item>
                <el-menu-item class="aoip" index="AncientRead" data-aoi-type="nav" data-aoi-desc="导航至古籍阅览页"
                    data-aoi-group="service-menu">古籍阅览</el-menu-item>
                <el-menu-item class="aoip" index="DiscRequest" data-aoi-type="nav" data-aoi-desc="导航至随书光盘页"
                    data-aoi-group="service-menu">随书光盘</el-menu-item>
                <el-menu-item class="aoip" index="DocumentTransfer" data-aoi-type="nav" data-aoi-desc="导航至文献传递页"
                    data-aoi-group="service-menu">文献传递</el-menu-item>
                <el-menu-item class="aoip" index="TechSearch" data-aoi-type="nav" data-aoi-desc="导航至科技查新页"
                    data-aoi-group="service-menu">科技查新</el-menu-item>
                <el-menu-item class="aoip" index="InfoTeaching" data-aoi-type="nav" data-aoi-desc="导航至文献检索教学页"
                    data-aoi-group="service-menu">文献检索教学</el-menu-item>
                <el-menu-item class="aoip key-aoi" index="SeatReserve" data-aoi-type="nav"
                    data-aoi-desc="导航至空间与设施(座位预约)页" data-aoi-group="service-menu">空间与设施</el-menu-item>
                <el-menu-item class="aoip" index="VolunteerTeam" data-aoi-type="nav" data-aoi-desc="导航至志愿服务团招募页"
                    data-aoi-group="service-menu">志愿服务团</el-menu-item>
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