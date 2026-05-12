<template>
    <div class="main-content">
        <div class="aoi breadcrumb">
            您当前所在位置 ： 首页 > 服务 > 空间与设施
        </div>
        <div class="aoi key-aoi title">
            <h2>座位预约</h2>
        </div>
        <div class="aoi key-aoi content">
            <p>欢迎使用座位预约系统，以下是座位预约的流程和使用方法：</p>
            <p>
                1. 本系统仅供本校学生使用，图书馆需通过刷卡或人脸识别进入。
            </p>
            <p>
                2. 点击“开始预约”按钮进入预约系统，选择您希望预约的图书馆分区。
            </p>
            <p>
                3. 选择您希望预约的日期和时间段，系统会显示可用的座位。
            </p>
            <p>
                4. 选择合适的座位并确认预约信息，点击“提交”按钮。
            </p>
            <p>
                5. 您的预约信息将通过邮件发送至您的邮箱，请及时查收。
            </p>
            <p>
                <strong>注意事项：</strong>
            </p>
            <p>
                - 请提前预约，避免高峰期座位紧张。
            </p>
            <p>
                - 如需取消预约，请在预约时间前24小时内进行操作。
            </p>
            <p>
                - 座位预约系统仅在工作日7:00-22:00开放，周末及节假日请提前安排。
            </p>
        </div>
        <div class="button-container">
            <button class="aoi key-aoi start-button" @click="navigateToReserve">开始预约</button>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const navigateToReserve = () => {
    router.push('/reserve');
};
</script>

<style scoped>
.title {
    text-align: center;
}

.main-content {
    padding: 20px 5%;
}

.content {
    text-indent: 2em;
    font-size: 18px;
    line-height: 2;
}

.content p {
    margin: 0;
}

.button-container {
    text-align: center;
    margin-top: 30px;
}

.start-button {
    font-size: 24px;
    padding: 10px 20px;
    background-color: #3597ff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.start-button:hover {
    background-color: #66aaf2;
}
</style>