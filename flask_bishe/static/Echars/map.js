var ec_center = echarts.init(document.getElementById('map'));

var mydata36316 = [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}]

var ec_center_option = {
    title: {
        text: '全国现有确诊',
        subtext: '',
        x: 'left'
    },

    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 1,end: 9 },
            {start: 10, end: 99 },
            { start: 100, end: 999 },
            {  start: 1000, end: 9999 },
            { start: 10000 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    //配置属性
    series: [{
        name: '现有确诊人数',
        type: 'map',
        mapType: 'china',
        roam: true, //拖动和缩放
        itemStyle: {
            normal: {
                borderWidth: .5, //区域边框宽度
                borderColor: '#62d3ff', //区域边框颜色
                areaColor: "#b7ffe6", //区域颜色
            },
            emphasis: { //鼠标滑过地图高亮的相关设置
                borderWidth: .5,
                borderColor: '#fff',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 18,
            }
        },
        data:[] //mydata //数据
    }]
};
ec_center.setOption(ec_center_option)