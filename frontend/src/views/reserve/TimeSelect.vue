<template>
    <div class="time-page">
        <div class="notice">
            <h3 class="aoi key-aoi" data-aoi-type="info" data-aoi-desc="预约时间规则提示标题" data-aoi-group="time-select">温馨提示：
            </h3>
            <ul class="aoi key-aoi" data-aoi-type="info" data-aoi-desc="预约时间范围及连续时段要求说明" data-aoi-group="time-select">
                <li><strong>预约时间范围：</strong>您可以预约的时间为今天起至未来一周内的任意一天。请确保您的预约在开放时间内。</li>
                <li><strong>开放时间：</strong>图书馆开放时间为每天的 <strong>7:30 AM</strong> 至 <strong>10:30 PM</strong>。请在此时间段内进行预约。
                </li>
                <li><strong>连续时段要求：</strong>所有预约均需选择连续的时段。请在预约时确保选择的时间段没有间断。</li>
            </ul>
        </div>
        <div class="datetime-picker">
            <div class="date-container">
                <div class="aoim key-aoi label" data-aoi-type="info" data-aoi-desc="预约日期选择标签"
                    data-aoi-group="time-select">预约日期：</div>
                <div class="date-box">
                    <el-config-provider :locale="locale">
                        <el-date-picker class="aoim key-aoi dp" v-model="selectedDate" type="date" placeholder="选择日期"
                            data-aoi-type="input" data-aoi-desc="选择具体的预约日期" data-aoi-group="time-select"
                            @change="handleDateChange" :default-value="new Date(1998, 12)" size="large"
                            :disabled-date="disabledDate" :editable="false" :popper-options="{
                                modifiers: [
                                    {
                                        name: 'flip',
                                        options: {
                                            fallbackPlacements: ['bottom'],
                                            allowedAutoPlacements: ['bottom'],
                                        }
                                    }
                                ]
                            }">
                        </el-date-picker>
                    </el-config-provider>
                </div>
            </div>
            <div class="time-selects">
                <div class="aoim key-aoi label" data-aoi-type="info" data-aoi-desc="预约时间段选择标签"
                    data-aoi-group="time-select">预约时间段：</div>
                <div class="time-box">
                    <el-time-select class="aoim key-aoi" v-model="startTime" :max-time="endTime" placeholder="起始时间"
                        data-aoi-type="input" data-aoi-desc="选择预约开始时间" data-aoi-group="time-select" start="07:30"
                        step="00:30" end="22:30" size="large" @change="handleTimeChange" :min-time="minTime" />
                    <span class="separator">至</span>
                    <el-time-select class="aoim key-aoi" v-model="endTime" :min-time="startTime" placeholder="结束时间"
                        data-aoi-type="input" data-aoi-desc="选择预约结束时间" data-aoi-group="time-select" start="07:30"
                        step="00:30" end="22:30" size="large" @change="handleTimeChange" />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { ElConfigProvider } from 'element-plus';
import zhCn from 'element-plus/es/locale/lang/zh-cn';
import { useStore } from 'vuex';

const store = useStore();

const selectedDate = ref(store.state.selectedDate);
const startTime = ref(store.state.startTime);
const endTime = ref(store.state.endTime);
const locale = zhCn;
const minTime = ref('07:29');

const disabledDate = (date) => {
    const today = new Date();
    const oneWeekLater = new Date();
    oneWeekLater.setDate(today.getDate() + 7);
    today.setHours(0, 0, 0, 0); // 设置时间为今天的开始时刻

    // 禁用今天之后一周以后的日期
    return date > oneWeekLater || date < today;
};

const handleDateChange = (date) => {
    const today = new Date();
    const selected = new Date(date);
    store.commit('setSelectedDate', date); // 提交 mutation 更新 selectedDate

    // 如果选择的日期是今天
    if (selected.setHours(0, 0, 0, 0) === today.setHours(0, 0, 0, 0)) {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0'); // 补零
        const minutes = String(now.getMinutes()).padStart(2, '0'); // 补零
        minTime.value = `${hours}:${minutes}`;
    } else {
        minTime.value = '07:29';  // 其他日期重置为默认时间
    }
};

const handleTimeChange = () => {
    store.commit('setStartTime', startTime.value); // 提交 mutation 更新 startTime
    store.commit('setEndTime', endTime.value); // 提交 mutation 更新 endTime
};
</script>

<style scoped>
.datetime-picker {
    display: flex;
    gap: 20px;
    padding: 20px;
}

.time-page {
    margin: 10px 150px;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.072);
    padding: 20px 60px;
}

.date-container {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.time-selects {
    flex: 1.5;
    display: flex;
    gap: 30px;
}

.label {
    margin: 10px 0;
    font-weight: bold;
    color: #333;
}

.time-select {
    flex: 1;
    display: flex;
    flex-direction: column;
}

.notice {
    padding: 5px 0;
    /* max-width: 600px; */
    margin: auto;
    border-bottom: 1px solid #33333338;
}

h3 {
    color: #333;
    margin: 5px 0;
}

ul {
    list-style-type: disc;
    margin-left: 20px;
    color: #555;
}

li {
    margin-bottom: 5px;
}

strong {
    color: #407fba;
}
</style>