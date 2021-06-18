// the script of controlling canvas

var ctx, color = "#000";

function initCanvas() {
    // initialize canvas pad
    console.log("Canvas Pad Loaded!");
    ctx = document.getElementById("paint").getContext("2d");
    ctx.strokeStyle = color;
    ctx.lineWidth = 5;

    drawTouch();
    drawPointer();
    drawMouse();
}

var drawTouch = function () {
    var start = function (e) {
        ctx.beginPath();
        x = e.changedTouches[0].pageX;
        y = e.changedTouches[0].pageY;
        ctx.moveTo(x, y);
    };
    var move = function (e) {
        e.preventDefault();
        x = e.changedTouches[0].pageX;
        y = e.changedTouches[0].pageY;
        ctx.lineTo(x, y);
        ctx.stroke();
    };
    document.getElementById("paint").addEventListener("touchstart", start, false);
    document.getElementById("paint").addEventListener("touchmove", move, false);
};

var drawPointer = function () {
    var start = function (e) {
        e = e.originalEvent;
        ctx.beginPath();
        x = e.pageX;
        y = e.pageY;
        ctx.moveTo(x, y);
    };
    var move = function (e) {
        e.preventDefault();
        e = e.originalEvent;
        x = e.pageX;
        y = e.pageY;
        ctx.lineTo(x, y);
        ctx.stroke();
    };
    document.getElementById("paint").addEventListener("MSPointerDown", start, false);
    document.getElementById("paint").addEventListener("MSPointerMove", move, false);
};

var drawMouse = function () {
    var clicked = 0;
    var start = function (e) {
        clicked = 1;
        ctx.beginPath();
        x = e.pageX;
        y = e.pageY;
        ctx.moveTo(x, y);
    };
    var move = function (e) {
        if (clicked) {
            x = e.pageX;
            y = e.pageY;
            ctx.lineTo(x, y);
            ctx.stroke();
        }
    };
    var stop = function (e) {
        clicked = 0;
    };
    document.getElementById("paint").addEventListener("mousedown", start, false);
    document.getElementById("paint").addEventListener("mousemove", move, false);
    document.addEventListener("mouseup", stop, false);
};