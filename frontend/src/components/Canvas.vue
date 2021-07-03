<template>
  <div>
    <!-- canvas component -->
    <div class="row">
      <div id="drawing q-pa-lg">
        <sign-canvas class="sign-canvas" ref="SignCanvas" :options="options" v-model="imgValue"/>
        <!-- <img v-if="imgValue" class="view-image" :src="imgValue" width="150" height="150" alt="result">-->
        <p id="result">Number: {{ result.digit }}</p>
        <p id="probability">Probability: {{ result.probability }}</p>
      </div>
      <div class="config q-pa-lg">
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
            <span class="item-label">兼容高分屏高清绘制:</span>
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
                        <input v-model="options.borderWidth" type="number">
                    </span>
          </li>
          <li class="li-c">
            <span class="item-label">下笔宽度:</span>
            <span class="item-content">
                        <input v-model="options.writeWidth" type="number">
                    </span>
          </li>
          <li class="li-c">
            <span class="item-label">图片类型:</span>
            <span class="item-content">
                        <input v-model="options.imgType" type="text">
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
                        <input type="color" v-model="options.writeColor">
                    </span>
          </li>
         
        </ul>
        <div class="sign-btns row-sm">
          <q-btn color="primary" id="clear" @click="canvasReset()">清空</q-btn>

        </div>
        <textarea class="q-mt-sm" name="base64-img" id="" cols="50" rows="10"
                  placeholder="the base64 code">{{ imgValue }}</textarea>
      </div>
    </div>

  </div>
</template>
<script>
import SignCanvas from 'sign-canvas';

export default {
  components: {SignCanvas},
  data() {
    return {
      imgValue: null, // base64 of the image
      result: {
        digit: null,
        probability: null,
      },
      options: {
        isFullScreen: false,   ////是否全屏手写 [Boolean] 可选
        isFullCover: false, //是否全屏模式下覆盖所有的元素 [Boolean] 可选 (这个有意思，可以研究一下怎么实现的)
        isDpr: false,       //是否使用dpr兼容高分屏 [Boolean] 可选
        isShowBorder: false, //是否显示边框 [可选]
        lastWriteSpeed: 1,  //书写速度 [Number] 可选
        lastWriteWidth: 2,  //下笔的宽度 [Number] 可选
        lineCap: 'round',   //线条的边缘类型 [butt]平直的边缘 [round]圆形线帽 [square]	正方形线帽
        lineJoin: 'bevel',  //线条交汇时边角的类型  [bevel]创建斜角 [round]创建圆角 [miter]创建尖角。
        canvasWidth: 280, //canvas宽高 [Number] 可选
        canvasHeight: 280,  //高度  [Number] 可选
        bgColor: '#fcc', //背景色 [String] 可选
        borderWidth: 1, // 网格线宽度  [Number] 可选
        borderColor: "#ff787f", //网格颜色  [String] 可选
        writeWidth: 5, //基础轨迹宽度  [Number] 可选
        maxWriteWidth: 30, // 写字模式最大线宽  [Number] 可选
        minWriteWidth: 5, // 写字模式最小线宽  [Number] 可选
        writeColor: '#101010', // 轨迹颜色  [String] 可选
        isSign: true, //签名模式 [Boolean] 默认为非签名模式,有线框, 当设置为true的时候没有任何线框
        imgType: 'png'   //下载的图片格式  [String] 可选为 jpeg  canvas本是透明背景的
      }
    }
  },
  watch: {
    'imgValue': function (newValue) {
      if (newValue) {
        let FormData = {
          imgValue: newValue.replace('data:image/png;base64,', '')
        };

        this.$axios
          .post('api/img/', FormData)
          .then(
            response => {
              this.result.digit = response.data.number;
              this.result.probability = response.data.probability;
            }
          ).catch(
          function (error) {
            console.log("(Reach backend) " + error)
          }
        )
      }
    }
  },
  mounted() {
    // Test backend server connection
    this.$axios
      .get('api/')
      .then(
        response => {
          this.networkPopup(response.status)
        }
      ).catch(
      function (error) {
        console.log(error);
        this.networkPopup(error);
      }.bind(this)
    )
  },
  methods: {
    // network status
    networkPopup(status) {
      if (status === 200) {
        this.$q.notify({
          message: 'Good to go',
          caption: 'Backend server connected',
          color: 'green',
          icon: 'done'
        })
      } else {
        this.$q.dialog({
          title: 'Cannot connect Backend Server',
          message: `Error message:\n ${status.message}`,
          position: 'bottom',
          persistent: true
        }).onDismiss(() => {
          console.log('.')
          this.$q.notify({
            message: 'This program may not be functional as expected',
            caption: 'Refresh and try again',
            color: 'red',
            icon: 'warning'
          })
        })
      }
    },
    // reset canvas
    canvasReset() {
      this.$refs.SignCanvas.canvasClear();
      this.result.digit = null;
      this.result.probability = null;
    }
  }
}
</script>
<style lang="sass">
.sign-canvas
  display: block
  margin: 20px auto


.view-image
  display: block
  margin: 20px auto


.config
  margin: 20px auto

  .ul-config
    .li-c
      display: flex
      align-items: center
      padding: 4px 10px

      .item-content
        margin-left: 10px

.sign-btns
  > button
    margin: 2px
</style>
