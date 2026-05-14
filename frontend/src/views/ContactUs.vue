<template>
    <div class="main-box">
        <div class="sidebar">
            <div class="bar-title">
                <h2 class="aoi" data-aoi-type="info" data-aoi-desc="侧边栏标题-联系我们" data-aoi-group="contact-sidebar">
                    联系我们
                </h2>
            </div>
        </div>
        <div class="main-content">
            <div class="title">
                <h1 class="aoi" data-aoi-type="info" data-aoi-desc="页面主标题-联系我们" data-aoi-group="contact-main">
                    联系我们
                </h1>
            </div>
            <div class="aoi content" data-aoi-type="info" data-aoi-desc="图书馆各部门联系方式、电话及咨询邮箱详情展示区"
                data-aoi-group="contact-details">
                <p style="margin-top: 20px;"><strong>一般问题咨询：</strong>010-67392185；010-67396505</p>
                <p style="margin-top: 5px;">
                    <strong>参观交流：</strong>010-67392063（请至少提前3个工作日预约，下载“来访预约单”，发送到yujinmei@bjut.edu.cn）
                </p>
                <p style="margin-top: 5px;"><strong>总服务台：</strong>010-67391819</p>
                <p style="margin-top: 5px;"><span style="color: red;"><strong>24小时应急电话<span
                                style="color: rgb(0, 0, 0);">：</span></strong></span>010-67396502</p>
                <p style="margin-top: 5px;"><strong>报名学生志愿团：</strong>010-67396516</p>

                <p style="text-align: center; margin-top: 20px; margin-bottom: 15px;"><strong>部门联系方式</strong></p>

                <div align="center">
                    <table class="MsoNormalTable" border="1" cellspacing="0" cellpadding="0" width="617"
                        style="width: 617px; border: none;">
                        <tbody>
                            <tr>
                                <td width="184" align="center" valign="middle">
                                    <p><b>部&nbsp;&nbsp;门</b></p>
                                </td>
                                <td width="220" align="center" valign="middle">
                                    <p><b>电&nbsp;&nbsp;话</b></p>
                                </td>
                                <td width="212.66666666666666" align="center" valign="middle">
                                    <p><b>电子邮箱</b></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="184" align="center" valign="middle">
                                    <p>综合办公室</p>
                                </td>
                                <td width="220" align="center" valign="middle">
                                    <p>010-67391819</p>
                                </td>
                                <td width="212.66666666666666" align="center" valign="middle">
                                    <p>lib@bjut.edu.cn</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="184" align="center" valign="middle">
                                    <p>文献建设部</p>
                                </td>
                                <td width="220" align="center" valign="middle">
                                    <p>010-67391823</p>
                                </td>
                                <td width="212.66666666666666" align="center" valign="middle">
                                    <p>lib-cb@bjut.edu.cn</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="184" align="center" valign="middle">
                                    <p>阅读推广部</p>
                                </td>
                                <td width="220" align="center" valign="middle">
                                    <p>010-67396516</p>
                                </td>
                                <td width="212.66666666666666" align="center" valign="middle">
                                    <p>lib-rb@bjut.edu.cn</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="184" align="center" valign="middle">
                                    <p>流通阅览部</p>
                                </td>
                                <td width="220" align="center" valign="middle">
                                    <p>010-67396505</p>
                                </td>
                                <td width="212.66666666666666" align="center" valign="middle">
                                    <p>lib-lb@bjut.edu.cn</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="184" align="center" valign="middle">
                                    <p>信息咨询部</p>
                                </td>
                                <td width="220" align="center" valign="middle">
                                    <p>010-67392185</p>
                                </td>
                                <td width="212.66666666666666" align="center" valign="middle">
                                    <p>ppzhou@bjut.edu.cn</p>
                                </td>
                            </tr>
                            <tr>
                                <td width="184" align="center" valign="middle">
                                    <p>技术部</p>
                                </td>
                                <td width="220" align="center" valign="middle">
                                    <p>010-67396501</p>
                                </td>
                                <td width="212.66666666666666" align="center" valign="middle">
                                    <p class="vsbcontent_end">lib-jsb@bjut.edu.cn</p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ContactUs',
};
</script>

<style scoped>
.title {
    text-align: center;
}

.main-box {
    background-color: rgba(255, 255, 255, 0.928);
    height: 95%;
    padding: 20px 200px;
    text-align: left;
    display: flex;
}

.sidebar {
    flex: 1;
}

.bar-title {
    background-size: cover;
    background-position: center;
    background-image: url(../assets/sidebar.png);
    text-align: center;
}

.main-content {
    flex: 3;
    padding: 0 5%;
}

.content{
    line-height: 1;
}
table{
    line-height: 0.5;
}

</style>