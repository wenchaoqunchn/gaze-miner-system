<template>
    <div class="aoi poster-container" data-aoi-type="info" data-aoi-desc="图书馆实景风貌轮播海报区" data-aoi-group="poster-player">
        <img :src="singleImage" alt="图书馆实景" class="poster-image" />
    </div>
</template>

<script>
import libimg from '../assets/player/zhongting.jpg';

export default {
    name: 'PosterPlayer',
    data() {
        return {
            singleImage: libimg,
        };
    },
};
</script>

<style scoped>
.poster-container {
    width: 100%;
    max-width: 700px;
    margin: auto;
}

.poster-image {
    width: 100%;
    height: 300px;
    object-fit: contain;
    border-radius: 5px;
}
</style>