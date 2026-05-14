<template>
    <el-steps class="aoi" :active="activeStep" finish-status="success" data-aoi-type="info"
        data-aoi-desc="通用流程步骤指示器整体区域" data-aoi-group="step-bar">
        <el-step class="aoim key-aoi" v-for="step in steps" :key="step.title" :title="step.title"
            :description="step.description" data-aoi-type="info" data-aoi-desc="具体流程步骤节点状态展示"
            data-aoi-group="step-bar" />
    </el-steps>
</template>

<script setup>
import { ref } from 'vue';

const activeStep = ref(0);

const steps = [
    { title: '步骤 1', description: '描述 1' },
    { title: '步骤 2', description: '描述 2' },
    { title: '步骤 3', description: '描述 3' },
];

const nextStep = () => {
    if (activeStep.value < steps.length - 1) {
        activeStep.value++;
    }
};

const prevStep = () => {
    if (activeStep.value > 0) {
        activeStep.value--;
    }
};
</script>

<style scoped>
.step-content {
    margin: 20px 0;
}

.buttons {
    display: flex;
    justify-content: space-between;
}
</style>