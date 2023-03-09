"use strict";

function randomColor() {
  var opacity = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : 1;
  var r = parseInt(Math.random() * 256);
  var g = parseInt(Math.random() * 256);
  var b = parseInt(Math.random() * 256);
  return "rgba(".concat(r, ", ").concat(g, ", ").concat(b, ", ").concat(opacity, ")");
}