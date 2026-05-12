<template>
  <div id="container">
    <div id="bg">
      <div id="tt" class="mg">本组实验完成</div>
      <div class="mg">
        <el-button type="primary" class="btn" @click="handleAnalyze">
          开始访谈
        </el-button>
        <el-button type="default" class="btn" @click="openHomePage">
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

const store = useStore();

// 使用 Vuex 状态
const skipReq = computed(() => store.state.skipRequest);

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

// 新增函数：打开首页
const openHomePage = () => {
  window.open('/', '_blank'); // 在新标签页打开首页
};

// 页面挂载后，延迟500毫秒自动执行 stop 操作
onMounted(() => {
  setTimeout(() => {
    handleStop();
  }, 500);
});

</script>

<style scoped>
#tt {
  color: #444;
  font-size: 50px;
  font-weight: bold;
}

#container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: #363636;
}

#bg {
  background-color: #ffffffda;
  border: 1px solid rgb(192, 192, 192);
  border-radius: 20px;
  width: 600px;
  height: 400px;
  padding: 20px;
}

.mg {
  margin: 20px;
}

.btn {
  border-radius: 15px;
  font-size: 50px;
  margin-top: 20px;
  padding: 50px;
}
</style>