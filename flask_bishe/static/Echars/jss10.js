

var chartDom = document.getElementById('box11');
var myChart3691 = echarts.init(chartDom);
var option;

option = {
  title: [
    {
      text: ''
    }
  ],
  polar: {
    radius: [30, '80%']
  },
  angleAxis: {
    //根据数据变换坐标轴，这里表示最大值，可以用function
    max: function(value) {
      if (value >= 100) {
        value = value / 100;
      }
    },
    startAngle: 75
  },
  radiusAxis: {
    type: 'category',
    data: []
  },
  series: {
    type: 'bar',
    data: [],
    coordinateSystem: 'polar',//coordinateSystem该系列使用的坐标系，可选：'cartesian2d'使用二维的直角坐标系（也称笛卡尔坐标系），通过 xAxisIndex, yAxisIndex指定相应的坐标轴组件。'polar'使用极坐标系，通过 polarIndex 指定相应的极坐标组件
    label: {
      show: true,
      position: 'middle',
      formatter: '{b}: {c}'
    }
  }
};
$.ajax({
  cache:false,
  type:"GET",
  url:"../static/beautifulsoup/json/worldTop6.json",
  dataType:"json",
  async:true,
  success:
    function (datas) {
    console.log(datas)
      return myChart3691.setOption({
        series:{
          name:'died',
          data:datas.died,

        },
        radiusAxis:{
          data:datas.area,
        }
      });
    },
   error:
    function (datas) {
    console.log(datas)
      return "false";
    }
});
option && myChart3691.setOption(option);
// $.getJSON('../static/beautifulsoup/json/diedTrueTopFive.json').done(function(datas){
//   myChart3691.setOption({
//     series:{
//       name:'died',
//       data:datas.died,
//
//     },
//     radiusAxis:{
//       data:datas.area,
//     }
//   });
// })



