// store/index.js
import { createStore } from 'vuex';

const store = createStore({
    state() {
        return {
            selectedFloor: null,  // 用户选择的层数
            selectedDate: '',     // 用户选择的日期
            startTime: '',        // 用户选择的起始时间
            endTime: '',          // 用户选择的结束时间
            selectedSeat: null,   // 用户选择的座位号
            staticSeats: [
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "available" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "available" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "available" },
                { status: "available" },
                { status: "booked" },
                { status: "available" },
                { status: "booked" },
                { status: "booked" },
                { status: "available" },
                { status: "booked" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "booked" },
                { status: "available" },
                { status: "booked" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "booked" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" },
                { status: "available" }
            ],
            staticF2: {
                "中文社科1区": {
                    "A": "马克思主义",
                    "B": "哲学、宗教",
                    "C": "社会科学总论",
                    "D": "政治、法律"
                },
                "中文社科2区": {
                    "D": "政治、法律",
                    "E": "军事",
                    "H": "语言、文字"
                },
                "中文社科3区": {
                    "K": "历史、地理",
                    "J": "艺术"
                },
                "中文社科4区": {
                    "J": "艺术",
                    "F": "经济",
                    "G": "文化、科学、教育、体育"
                }
            },
            staticF3: {
                "中文科技1區": {
                    "O": "數理科學和�學",// 引入乱码
                    "N": "□然科學總論",// 引入乱码
                    "�": "& lt; script& gt; alert(& quot; & quot;);& lt;/script&gt;"// 引入乱码
                },
                "中文科技2區": {
                    "O": "數理科學和化學",
                    "R": "�物科學",// 引入乱码
                    "S": "農業科學",
                    "P": "□文學、地球科學",// 引入乱码
                    "Q": "生物科學"
                },
                "中文科技3區": {
                    "TN": "電â€子技術、通訊技術",  // 引入乱码
                    "TP": "自動化技術、計算機â€技術", // 引入乱码
                    "TB": "工業技術",
                    "TG": "金屬學與金属工艺", // 引入乱码
                    "TH": "機械、仪表工業", // 引入乱码
                    "TM": "电工技術"
                },
            },
            staticF4: {
                "中文科技4區": {
                    "U": "交通運輸",
                    "X": "環境科學、安全科學â€", // 引入乱码
                    "Z": "綜合性圖書âœ”" // 引入乱码
                },
                "中文科技5區": {
                    "TU": "建築科學",
                    "TN": "電子技術、通信技術â€œ", // 引入乱码
                    "TQ": "化學工業",
                    "TS": "輕工業、手工業☻", // 引入乱码
                    "TV": "水利工Ã©程", // 引入乱码
                    "TW": "環境保護â†”" // 引入乱码
                },
                "文學區": {
                    "I": "文學â—",
                    "!Error": "[vue/compiler-sfc] Unterminated string constant. (92:14)",
                }
            },
            skipRequest: true,    // 开发设置
            noIssue: false,        // 开发设置
            exportAOI: false
        };
    },
    mutations: {
        setSelectedFloor(state, floor) {
            state.selectedFloor = floor;
        },
        setSelectedDate(state, date) {
            state.selectedDate = date;
        },
        setStartTime(state, time) {
            state.startTime = time;
        },
        setEndTime(state, time) {
            state.endTime = time;
        },
        setSelectedSeat(state, seat) {
            state.selectedSeat = seat;
        },
        setStaticSeats(state, seats) {
            state.staticSeats = seats;
        },
        toggleSkipRequest(state) {
            state.skipRequest = !state.skipRequest;
        },
        toggleNoIssue(state) {
            state.noIssue = !state.noIssue;
        },
        toggleExportAOI(state, value) { // 新增的 mutation
            state.exportAOI = value; // 直接设置为传入的值
        },
    },
    actions: {
        updateSelectedFloor({ commit }, floor) {
            commit('setSelectedFloor', floor);
        },
        updateSelectedDate({ commit }, date) {
            commit('setSelectedDate', date);
        },
        updateStartTime({ commit }, time) {
            commit('setStartTime', time);
        },
        updateEndTime({ commit }, time) {
            commit('setEndTime', time);
        },
        updateSelectedSeat({ commit }, seat) {
            commit('setSelectedSeat', seat);
        },
        updateStaticSeats({ commit }, seats) {
            commit('setStaticSeats', seats);
        },
        toggleSkipRequest({ commit }) {
            commit('toggleSkipRequest');
        },
        toggleNoIssue({ commit }) {
            commit('toggleNoIssue');
        },
        toggleExportAOI({ commit }, value) { // 新增的 action
            commit('toggleExportAOI', value); // 提交 mutation
        },
    },
});

export default store;