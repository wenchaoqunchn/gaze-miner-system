<template>
    <div class="main-content">
        <div class="aoi breadcrumb" data-aoi-type="info" data-aoi-desc="面包屑位置提示" data-aoi-group="lib-layout">
            您当前所在位置 ： 首页 > 图书馆概况 > 图书馆布局
        </div>
        <div class="aoi title" data-aoi-type="info" data-aoi-desc="页面主标题-图书馆布局" data-aoi-group="lib-layout">
            <h2>图书馆布局</h2>
        </div>
        <div class="aoi content" data-aoi-type="info" data-aoi-desc="图书馆各楼层平面布局图的轮播展示区" data-aoi-group="lib-layout">
            <el-carousel height="65vh" type="card" arrow="always" indicator-position="none" :autoplay="false">
                <el-carousel-item>
                    <img src="../../assets/layout/f2.jpg" alt="图书馆布局2" class="carousel-image" />
                </el-carousel-item>
                <el-carousel-item>
                    <img src="../../assets/layout/f3.jpg" alt="图书馆布局3" class="carousel-image" />
                </el-carousel-item>
                <el-carousel-item>
                    <img src="../../assets/layout/f4.jpg" alt="图书馆布局4" class="carousel-image" />
                </el-carousel-item>
            </el-carousel>
        </div>
    </div>
</template>

<script setup>
// Import Element Plus components
import { ElCarousel, ElCarouselItem } from 'element-plus';
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

.carousel-image {
    width: auto;
    height: 100%;
    object-fit: cover;
    /* 保持图片比例 */
}
</style>