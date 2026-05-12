<template>
    <div class="main-content">
        <div class="aoi breadcrumb">
            您当前所在位置 ： 首页 > 图书馆概况 > 图书馆布局
        </div>
        <div class="aoi title">
            <h2>图书馆布局</h2>
        </div>
        <div class="aoi content">
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