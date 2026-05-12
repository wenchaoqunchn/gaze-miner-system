<template>
  <div class="ready-container">
    <div class="ready-card">
      <div class="header">
        <h1 class="title">系统实验配置</h1>
        <p class="subtitle">进入图书馆任务系统前的基础环境设置</p>
      </div>

      <div class="config-form">
        <!-- 模式配置 -->
        <div class="config-item">
          <div class="config-label">
            <span>运行模式</span>
            <span class="desc">选择全新记录或分析原有实验数据</span>
          </div>
          <div class="config-content">
            <el-radio-group v-model="isNewSession">
              <el-radio :label="true" border>创建新数据集</el-radio>
              <el-radio :label="false" border>分析已有数据</el-radio>
            </el-radio-group>

            <div v-show="!isNewSession" class="sub-config">
              <span class="sub-label">指定数据集编号：</span>
              <el-input-number v-model="num" :min="1" :max="99" size="small" />
            </div>
          </div>
        </div>

        <!-- 后端同步开关 -->
        <div class="config-item">
          <div class="config-label">
            <span>后端API请求</span>
            <span class="desc">开启后将向后端正常发送API请求</span>
          </div>
          <div class="config-content">
            <!-- skipReq 为 false 代表“开启同步系统”，true 代表“跳过/停用” -->
            <el-switch v-model="skipReq" :active-value="false" :inactive-value="true" active-text="开启"
              inactive-text="停用" />
          </div>
        </div>

        <!-- AOI开关 -->
        <div class="config-item">
          <div class="config-label">
            <span>AOI 信息导出</span>
            <span class="desc">自动计算并导出交互组件的区域数据字典</span>
          </div>
          <div class="config-content">
            <el-switch v-model="exportAOI" active-text="开启" inactive-text="停用" />
          </div>
        </div>
      </div>

      <div class="footer">
        <el-button type="primary" class="enter-btn" @click="handleClick">
          进入图书馆任务系统 >
        </el-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import { ElMessage } from 'element-plus';

const store = useStore();
const router = useRouter();

// 控制是否是新会话的开关，默认为 true (创建新数据集)
const isNewSession = ref(true);
// 从 1 开始，作为已有数据集的编号输入 (当上方选为 false 时生效)
const num = ref(1);

const skipReq = computed({
  get: () => store.state.skipRequest,
  set: (value) => store.commit('toggleSkipRequest', value),
});

const exportAOI = computed({
  get: () => store.state.exportAOI,
  set: (value) => store.commit('toggleExportAOI', value),
});

// 在组件挂载时，强制将请求跳过变量置为 false，确保默认处于开启发送请求的状态
onMounted(() => {
  store.commit('toggleSkipRequest', false);
});

// 处理点击事件，底层传递链路维持不变
const handleClick = () => {
  // 核心逻辑：如果选了"新建数据集"，就发 focus_session: 0；否则发指定的旧编号
  const sessionIndex = isNewSession.value ? 0 : num.value;

  if (!skipReq.value) {
    axios
      .post("/api/init", { focus_session: sessionIndex, exportAOI: exportAOI.value })
      .then((response) => {
        console.log(response);
        return axios.post("/api/start");
      })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.error('Error during the API call:', error);
      });
  } else {
    ElMessage.success('API 请求已被跳过');
  }

  // 跳转到新路由
  router.push({ name: 'HomePage' });
};
</script>

<style scoped>
.ready-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100vw;
  background: linear-gradient(135deg, #2b323b 0%, #43515f 100%);
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

.ready-card {
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
  width: 100%;
  max-width: 650px;
  padding: 50px 40px;
  box-sizing: border-box;
}

.header {
  text-align: center;
  margin-bottom: 40px;
}

.title {
  color: #2c3e50;
  font-size: 32px;
  font-weight: bold;
  margin: 0 0 12px 0;
}

.subtitle {
  color: #7f8c8d;
  font-size: 16px;
  margin: 0;
}

.config-form {
  display: flex;
  flex-direction: column;
  gap: 25px;
  margin-bottom: 40px;
}

.config-item {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding-bottom: 20px;
  border-bottom: 1px solid #ecf0f1;
}

.config-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.config-label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-right: 20px;
}

.config-label span {
  font-size: 17px;
  color: #34495e;
  font-weight: bold;
}

.config-label .desc {
  font-size: 13px;
  color: #95a5a6;
  font-weight: normal;
}

.config-content {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 12px;
}

.sub-config {
  display: flex;
  align-items: center;
  background: #f8f9fa;
  padding: 10px 15px;
  border-radius: 8px;
  border: 1px solid #e0e6ed;
  animation: fadeIn 0.3s ease-out;
}

.sub-label {
  font-size: 14px;
  color: #7f8c8d;
  margin-right: 10px;
}

.footer {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.enter-btn {
  width: 100%;
  font-size: 20px;
  padding: 26px 0;
  border-radius: 8px;
  font-weight: bold;
  letter-spacing: 2px;
  transition: all 0.3s ease;
}

.enter-btn:hover {
  box-shadow: 0 6px 15px rgba(64, 158, 255, 0.4);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-5px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>