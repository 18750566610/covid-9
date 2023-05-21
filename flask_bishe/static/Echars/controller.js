function showTime() {
    var date = new Date()
    var year = date.getFullYear()
    var month = date.getMonth()+1
    var day = date.getDate()
    var hour = date.getHours()
    var minute = date.getMinutes()
    var second = date.getSeconds()
    if(hour < 10){ hour = "0"+hour}
    if(minute < 10){ minute = "0"+minute}
    if(second < 10){ second = "0"+second}
    var time = year + "年"+ month + "月"+day + "日"+hour + ":"+minute + ":"+second
    $("#tim").html(time)
}

setInterval(showTime,1000) //1秒调用1次



function get_c2_data() {
    $.ajax({
        url:"/c2",
        success: function(data) {
            ec_center_option.series[0].data=data.data
            ec_center_option.series[0].data.push({
                name:"南海诸岛",value:0,
                itemStyle:{
                    normal:{ opacity:0},
                },
                label:{show:false}
            })
            ec_center.setOption(ec_center_option)
        },
        error: function(xhr, type, errorThrown) {

        }
    })
}

function get_l1_data() {
    ec_left1.showLoading()
    $.ajax({
        url:"/l1",
        success: function(data) {
            ec_left1_Option.xAxis[0].data=data.day
            ec_left1_Option.series[0].data=data.confirm_add
            ec_left1_Option.series[1].data=data.suspect_add
            ec_left1.setOption(ec_left1_Option)
            ec_left1.hideLoading()
        },
        error: function(xhr, type, errorThrown) {
        }
    })
}


function get_r1_data() {
    $.ajax({
        url: "/r1",
        success: function (data) {
            ec_right1_option.xAxis.data=data.city;
            ec_right1_option.series[0].data=data.confirm;
            ec_right1.setOption(ec_right1_option);
        }
    })
}

function refreshPage(){
    window.location.reload()
}

get_c2_data()
get_l1_data()
get_r1_data()