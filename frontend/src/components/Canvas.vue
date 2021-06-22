<template>
  <div>
    <sign-canvas class="sign-canvas" ref="SignCanvas" :options="options" v-model="value"/>
    <img v-if="value" class="view-image" :src="value" width="150" height="150" alt=""/>
    <div class="config">
      <ul class="ul-config">
        <li class="li-c">
          <span class="item-label">书写速度:</span>
          <span class="item-content">
                        <select name="isSign" v-model="options.isSign">
                            <option :value="true">签名</option>
                            <option :value="false">写字</option>
                        </select>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">显示边框/网格:</span>
          <span class="item-content">
                        <select name="isSign" v-model="options.isShowBorder">
                            <option :value="true">显示</option>
                            <option :value="false">不显示</option>
                        </select>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">兼容高倍屏高清绘制:</span>
          <span class="item-content">
                        <select name="isSign" v-model="options.isDpr">
                            <option :value="true">启用</option>
                            <option :value="false">关闭</option>
                        </select>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">边框宽度:</span>
          <span class="item-content">
                        <input v-model="options.borderWidth" type="number"/>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">下笔宽度:</span>
          <span class="item-content">
                        <input v-model="options.writeWidth" type="number"/>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">图片类型:</span>
          <span class="item-content">
                        <input v-model="options.imgType" type="text"/>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">线条的边缘类型:</span>
          <span class="item-content">
                        <select name="lineCap" v-model="options.lineCap">
                            <option value="butt">平直的边缘</option>
                            <option value="round">圆形线帽</option>
                            <option value="square">正方形线帽</option>
                        </select>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">线条交汇时边角的类型:</span>
          <span class="item-content">
                        <select name="lineCap" v-model="options.lineJoin">
                            <option value="bevel">创建斜角</option>
                            <option value="round">创建圆角</option>
                            <option value="miter">创建尖角</option>
                        </select>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">画笔颜色:</span>
          <span class="item-content">
                        <input type="color" v-model="options.writeColor"/>
                    </span>
        </li>
        <li class="li-c">
          <span class="item-label">背景色:</span>
          <span class="item-content">
                        <input type="color" v-model="options.bgColor"/>
                    </span>
        </li>
      </ul>
    </div>
    <div class="sign-btns">
      <span id="clear" @click="canvasClear()">清空</span>
      <span id="save" @click="saveAsImg()">保存</span>
      <span id="download" @click="downloadSignImg()">下载</span>
    </div>
  </div>
</template>

<script>
import SignCanvas from 'sign-canvas';

export default {
  name: "Canvas",
  components: {
    SignCanvas,
  },
  props: {},
  data() {
    return {
      value: null,
      options: {
        isFullScreen: false,   ////是否全屏手写 [Boolean] 可选
        isFullCover: false, //是否全屏模式下覆盖所有的元素 [Boolean]   可选
        isDpr: false,       //是否使用dpr兼容高分屏 [Boolean] 可选
        lastWriteSpeed: 1,  //书写速度 [Number] 可选
        lastWriteWidth: 2,  //下笔的宽度 [Number] 可选
        lineCap: 'round',   //线条的边缘类型 [butt]平直的边缘 [round]圆形线帽 [square]	正方形线帽
        lineJoin: 'bevel',  //线条交汇时边角的类型  [bevel]创建斜角 [round]创建圆角 [miter]创建尖角。
        canvasWidth: 280, //canvas宽高 [Number] 可选
        canvasHeight: 280,  //高度  [Number] 可选
        isShowBorder: true, //是否显示边框 [可选]
        bgColor: "#fff", //背景色 [String] 可选
        borderWidth: 1, // 网格线宽度  [Number] 可选
        borderColor: "#ff787f", //网格颜色  [String] 可选
        writeWidth: 5, //基础轨迹宽度  [Number] 可选
        maxWriteWidth: 30, // 写字模式最大线宽  [Number] 可选
        minWriteWidth: 5, // 写字模式最小线宽  [Number] 可选
        writeColor: '#101010', // 轨迹颜色  [String] 可选
        isSign: true, //签名模式 [Boolean] 默认为非签名模式,有线框, 当设置为true的时候没有任何线框
        imgType: 'jpeg'   //下载的图片格式  [String] 可选为 jpeg  canvas本是透明背景的
      }
    }
  },
  methods: {
    /**
     * 清除画板
     */
    canvasClear() {
      this.$refs.SignCanvas.canvasClegetContextar();
    },
    /**
     * 保存图片
     */
    saveAsImg() {
      const img = this.$refs.SignCanvas.saveAsImg();
      alert(`image 的base64：${img}`);
    },
    /**
     * 下载图片
     */
    downloadSignImg() {
      this.$refs.SignCanvas.downloadSignImg();
    },
    /**
     * 下载dealImage图片
     */
    dealImage() {
      this.$refs.SignCanvas.dealImage();
    },
  }


}
</script>

<style scoped lang="sass">
.sign-canvas
  background: #fff

</style>
