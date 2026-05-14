<template>
  <div class="page-container">
    <div class="content-card">
      <h1 class="title">本组实验完成</h1>

      <div class="actions" v-if="isMasterMode">
        <el-button type="warning" class="action-btn" @click="handleExportAOIInfo">
          导出全局AOI信息
        </el-button>
      </div>

      <div class="actions">
        <el-button type="primary" class="action-btn" @click="handleAnalyze">
          开始访谈
        </el-button>
        <el-button class="action-btn" @click="openHomePage">
          在新窗口打开首页
        </el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus';
import axios from 'axios';
import { useStore } from 'vuex';
import { computed, onMounted } from 'vue';
import { downloadJSON } from '../getAOIInfo.js'; // 确保引入了下载工具

const store = useStore();
const isMasterMode = computed(() => store.state.exportAOI);
const skipReq = computed(() => store.state.skipRequest);

// 导出逻辑
const handleExportAOIInfo = () => {
  const masterData = store.state.globalAOIMap;
  if (Object.keys(masterData).length === 0) {
    ElMessage.warning('AOI信息列表为空');
    return;
  }
  downloadJSON(masterData, 'AOI.json');
  ElMessage.success('全部AOI信息已导出');
};

const handleStop = () => {
  if (!skipReq.value) {
    axios
      .post("/api/stop")
      .then((response) => {
        if (response.status === 200) {
          ElMessage.success('眼动监测已成功停止！');
        }
      })
      .catch((error) => {
        console.error('Error during the stop API call:', error);
        ElMessage.error('眼动监测停止失败。');
      });
  } else {
    ElMessage.success('API 请求已被跳过');
  }
};

const handleAnalyze = () => {
  if (skipReq.value === false) {
    axios
      .post("/api/analyze")
      .then((response) => {
        if (response.status === 200) {
          ElMessage.success('分析成功！');
        }
      })
      .catch((error) => {
        console.error('Error during the analyze API call:', error);
        ElMessage.error('分析操作失败，请重试。');
      });
  } else {
    ElMessage.success('API 请求已被跳过');
  }
};

// 打开首页
const openHomePage = () => {
  window.open('/', '_blank');
};

// 页面挂载后，延迟500毫秒自动执行 stop 操作
onMounted(() => {
  setTimeout(() => {
    handleStop();
  }, 500);
});
</script>

<style scoped>
/* 外层容器：占满全屏，居中对齐 */
.page-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100%;
  background-color: #363636;
  padding: 20px;
  box-sizing: border-box;
}

/* 核心内容卡片：优雅的圆角和阴影，限制最大宽度 */
.content-card {
  background-color: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  width: 100%;
  max-width: 600px;
  padding: 50px 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
  /* 元素之间的统一间距 */
  box-sizing: border-box;
}

/* 标题：响应式字体大小，介于 30px 到 50px 之间 */
.title {
  color: #333;
  font-size: clamp(30px, 5vw, 50px);
  font-weight: bold;
  margin: 0;
  text-align: center;
}

/* 按钮组：支持自动换行，避免窄屏下挤压 */
.actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  width: 100%;
}

/* 按钮样式：调整了原本过大的 padding，保留大气的点击区域 */
.action-btn {
  border-radius: 12px;
  font-size: clamp(18px, 3vw, 24px);
  /* 字体适度缩放 */
  padding: 20px 40px;
  height: auto;
  margin: 0;
  /* 移除外边距，交给父级的 gap 处理 */
  flex: 1 1 auto;
  /* 允许按钮在小屏幕上撑满单行 */
  min-width: 200px;
  /* 保证按钮不会太窄 */
}
</style>