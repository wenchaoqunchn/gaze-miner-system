<template>
    <div class="aoi poster-container">
        <img :src="singleImage" alt="图书馆外景" class="poster-image" />
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