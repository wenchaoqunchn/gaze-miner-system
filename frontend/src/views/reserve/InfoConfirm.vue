<template>
    <!-- 提示信息 -->
    <div class="aoip key-aoi alert-message">
        <span class="alert-icon">⚠️</span> <!-- 使用 emoji 作为图标 -->
        请认真确认预约信息
    </div>
    <div class="info-box">
        <div class="info-container">
            <h2 class="aoim key-aoi">预约信息</h2>
            <p class="aoim key-aoi"><strong>层数：</strong> {{ selectedFloor }}</p>
            <p class="aoim key-aoi"><strong>日期：</strong> {{ formattedDate }}</p>
            <p class="aoim key-aoi"><strong>时间：</strong> {{ startTime }} - {{ endTime }}</p>
            <p class="aoim key-aoi"><strong>座位号：</strong> {{ selectedSeat }}</p>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';

const store = useStore();

// 使用 Vuex 状态
const selectedFloor = computed(() => store.state.selectedFloor);
const startTime = computed(() => store.state.startTime);
const endTime = computed(() => store.state.endTime);
const selectedSeat = computed(() => store.state.selectedSeat);
const selectedDate = computed(() => store.state.selectedDate);

// 计算属性，用于格式化日期
const formattedDate = computed(() => {
    const date = new Date(selectedDate.value);
    return date.toLocaleDateString('zh-HK', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });
});
</script>

<style scoped>

.alert-message {
    margin-top: 1rem;
    padding: 10px;
    background-color: #ddf1ff;
    /* 浅红色背景 */
    color: #0077d8;
    /* 红色文字 */
    border: 1px solid #0097d8;
    /* 红色边框 */
    border-radius: 5px;
    display: flex;
    align-items: center;
    /* 垂直居中对齐 */
    margin: 0 400px;
}

.alert-icon {
    margin-right: 8px;
    /* 图标与文本之间的间距 */
    color: #0090d8;
    /* 红色图标 */
    font-size: 1.5rem;
    /* 图标大小 */
}
.info-box {
    display: flex;
    justify-content: center;
    margin: 20px;
}

.info-container {
    background-color: #0000000d;
    /* 浅蓝色背景 */
    border: 1px solid #c4c4c4;
    /* 边框颜色 */
    border-radius: 12px;
    /* 圆角 */
    padding: 25px;
    /* 内边距 */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    /* 更柔和的阴影 */
    width: 320px;
    /* 宽度 */
    text-align: left;
    /* 左对齐 */
    transition: transform 0.3s;
    /* 动画效果 */
}


h2 {
    margin-bottom: 15px;
    /* 标题和内容之间的间距 */
    color: #0277bd;
    /* 标题颜色 */
    font-family: 'Arial', sans-serif;
    /* 字体 */
    font-weight: bold;
    /* 加粗 */
}

p {
    margin: 8px 0;
    /* 段落之间的间距 */
    font-size: 18px;
    /* 字体大小 */
    color: #c7c6c65c;
    /* 段落颜色 */
    line-height: 1.5;
    /* 行高 */
    user-select: text !important;
}

/* p:hover{
    color: #383838a9;
} */

strong {
    color: #d7d9dba4;
    /* 加粗文本的颜色 */
    user-select: text !important;
}
</style>