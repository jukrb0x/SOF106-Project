<template>
  <div>
    <!-- canvas component -->
    <div class="main">
      <div id="drawing q-px-lg">
        <sign-canvas
          class="sign-canvas"
          ref="SignCanvas"
          :options="options"
          v-model="imgValue"
        />
        <!-- <img v-if="imgValue" class="view-image" :src="imgValue" width="150" height="150" alt="result">-->
        <div class="results flex flex-center">

          <span v-if="isBrew">Brewing...</span>
          <span v-else-if="result.digit" id="result">Number: {{ result.digit }}</span>
          <span v-else>Please write a number above.</span>
        </div>
        <!--        <p id="probability">Probability: {{ result.probability }}</p>-->
      </div>
      <div class="q-px-lg q-pa-lg col content-center justify-sm-start">
        <div class="row content-center">
          <span class="option-title">Brush size:</span>
          <div class="q-gutter-sm">
            <q-input
              name="brush-size"
              v-model="options.writeWidth"
              dense
            ></q-input>
          </div>
        </div>
        <div class="row content-center">
          <span class="option-title">High DPI:</span>
          <div class="q-gutter-sm">
            <q-toggle :label="`${dprLabel}`" v-model="options.isDpr"/>
          </div>
        </div>
        <div class="flex justify-between">
          <div class="row content-center" style="height: 40px">
            <span class="option-title">Brush color:</span>
            <input type="color" class="q-ml-sm" v-model="options.writeColor"/>
          </div>

          <div class="row content-center">
            <q-btn color="primary" id="clear" @click="canvasReset">Clear</q-btn>
          </div>
        </div>
        <div class="row content-center q-py-lg">
          <span class="option-title">Local server:</span>
          <q-toggle :label="`${isLocalLabel}`" v-model="isLocal"/>
        </div>
        <div v-if="isLocal" class="row content-center" style="height: 40px">
          <span class="option-title q-mr-sm" style="max-width: 40px">Port:</span>
          <q-input name="brush-size" style="max-width: 170px" v-model="localPort" dense></q-input>
          <q-btn color="green" class="q-mx-sm" label="connect" @click="connectTest(networkPopup,networkPopup)"
                 dense></q-btn>
        </div>
        <div v-if="!isLocal" class="row content-center" style="height: 40px">
          <span class="option-title q-mr-sm" style="max-width: 40px">Host:</span>
          <q-input name="host-server" v-model="host" style="max-width: 170px" dense></q-input>
          <q-btn color="green" class="q-mx-sm" label="connect" @click="connectTest(networkPopup,networkPopup)"
                 dense></q-btn>
        </div>

      </div>
    </div>

  </div>
</template>
<script>
import SignCanvas from "sign-canvas";
import { debounce } from "quasar";

export default {
  components: { SignCanvas },
  data() {
    return {
      isLocal: false,
      localPort: "8000",
      host: "https://",
      imgValue: null, // base64 of the image
      result: {
        digit: null,
        probability: null
      },
      isBrew: false,
      options: {
        isFullScreen: false, ////是否全屏手写 [Boolean] 可选
        isFullCover: false, //是否全屏模式下覆盖所有的元素 [Boolean] 可选 (这个有意思，可以研究一下怎么实现的)
        isDpr: false, //是否使用dpr兼容高分屏 [Boolean] 可选
        isShowBorder: false, //是否显示边框 [可选]
        lastWriteSpeed: 1, //书写速度 [Number] 可选
        lastWriteWidth: 2, //下笔的宽度 [Number] 可选
        lineCap: "round", //线条的边缘类型 [butt]平直的边缘 [round]圆形线帽 [square]	正方形线帽
        lineJoin: "bevel", //线条交汇时边角的类型  [bevel]创建斜角 [round]创建圆角 [miter]创建尖角。
        canvasWidth: 280, //canvas宽高 [Number] 可选
        canvasHeight: 280, //高度  [Number] 可选
        bgColor: "#fcc", //背景色 [String] 可选
        borderWidth: 1, // 网格线宽度  [Number] 可选
        borderColor: "#ff787f", //网格颜色  [String] 可选
        writeWidth: 5, //基础轨迹宽度  [Number] 可选
        maxWriteWidth: 30, // 写字模式最大线宽  [Number] 可选
        minWriteWidth: 5, // 写字模式最小线宽  [Number] 可选
        writeColor: "#101010", // 轨迹颜色  [String] 可选
        isSign: true, //签名模式 [Boolean] 默认为非签名模式,有线框, 当设置为true的时候没有任何线框
        imgType: "png" //下载的图片格式  [String] 可选为 jpeg  canvas本是透明背景的
      }
    };
  },
  computed: {
    HostServer: function () {
      if (this.isLocal) {
        let ret;
        ret = `http://localhost:${ this.localPort }/`
        console.log("Backend Server: ", ret)
        return ret;
      } else {
        let ret;
        ret = `${ this.host }/`
        console.log("Backend Server: ", ret)
        return ret;
      }
    },
    dprLabel: function () {
      return this.options.isDpr ? "ON" : "OFF";
    },
    isLocalLabel: function () {
      return this.isLocal ? "ON" : "OFF";
    }
  },
  watch: {
    imgValue: function (newValue) {
      if (newValue) {
        this.result.digit = null;
        this.isBrew = true;
        let FormData = {
          imgValue: newValue.replace("data:image/png;base64,", "")
        };

        this.$axios
          .post(this.HostServer + "api/img/", FormData)
          .then(response => {
            this.result.digit = response.data.number;
            this.result.probability = response.data.probability;
          })
          .catch(function (error) {
            console.log("(Reach backend) " + error);
            //  figure out a way to callback networkPopup
          }).finally(() => {
            this.isBrew = false
          }
        );
      }
    },
    isLocal: function (newValue) {
      if (newValue) {
        this.connectTest(this.networkPopup, this.networkPopup);
      } else {
        if (this.host === 'http://' || this.host === 'https://' || this.host === '' || !this.host) {
          this.$q.notify({
            message: "If you have a cloud deployment...",
            caption: "Please fill up the complete host server address",
            color: "yellow",
            textColor: 'black',
            icon: "warning"
          })
        }
      }
    },
    // localPort: debounce(function () {
    //   this.connectTest(this.networkPopup, this.networkPopup);
    // }, 1000)
  },
  mounted() {
    // Test pre-deployed backend server connection
    // pre-deployed backend server
    this.host = 'https://ai.wh0.is';
    this.connectTest(this.networkPopup, this.preBackendFailed);
  },
  methods: {
    // backend server test
    connectTest(callback, errCallback) {
      this.$axios
        .get(this.HostServer + "api/")
        .then(response => {
          let ret = response.status;
          if (callback) {
            callback(ret);
          }
        })
        .catch(error => {
          console.log(error);
          if (callback) {
            errCallback(error);
          }
        });
    },
    // network status popup
    networkPopup(status) {
      // FIXME: I dealt with the error in the same function, which is improper.
      // console.log("stat ", status);
      if (status === 200) {
        this.$q.notify({
          message: "Good to go",
          caption: "Backend server connected",
          color: "green",
          icon: "done"
        });
      } else {
        this.$q
          .dialog({
            title: "Cannot connect to Backend Server",
            message: `Error message:\n ${ status.message }`,
            position: "bottom",
            persistent: false
          })
          .onDismiss(() => {
            this.$q.notify({
              message: "This program may not be functional as expected",
              caption: "Refresh and try again",
              color: "red",
              icon: "warning"
            });
          });
      }
    },
    // mounted test err callback (pre-deployed server test)
    preBackendFailed() {
      // if cloud server could not be connected
      this.host = "https://";
      this.isLocal = true;
    },
    // reset canvas
    canvasReset() {
      this.$refs.SignCanvas.canvasClear();
      this.result.digit = null;
      // this.result.probability = null;
      this.isBrew = false;
    }
  }
};
</script>
<style lang="sass">
.main
  display: flex
  flex-direction: row
  @media (max-width: $breakpoint-xs-max)
    flex-direction: column

.sign-canvas
  display: block
  margin: 20px auto

.option-title
  display: flex
  justify-content: start
  align-items: center
  width: 90px

.view-image
  display: block
  margin: 20px auto
</style>
