/**
 * 绑定事件
 * @param {HTMLElement} elem 待绑定事件的元素
 * @param {String} en 事件的名称
 * @param {Function} fn 回调函数
 * @param {Boolean} capture 是否使用事件捕获
 */
function bind(elem, en, fn, capture) {
	if (elem.addEventListener) {
		elem.addEventListener(en, fn, capture);
	} else {
		elem.attachEvent('on' + en, fn);
	}
}

/**
 * 反绑定事件
 * @param {HTMLElement} elem 待反绑定事件的元素
 * @param {String} en 事件的名称
 * @param {Function} fn 回调函数
 */
function unbind(elem, en, fn) {
	if (elem.removeEventListener) {
		elem.removeEventListener(en, fn);
	} else {
		elem.detachEvent('on' + en, fn);
	}
}

/**
 * 事件对象预处理
 * @param {Event} evt 事件对象
 */
function prepare(evt) {
	evt = evt || window.event;
	evt.target = evt.target || evt.srcElement;
	evt.preventDefault = evt.preventDefault || function() {
		this.returnValue = false;
	};
	return evt;
}

/**
 * 阻止事件的默认行为
 * @param {Event} evt 事件对象
 */
function prevent(evt) {
	if (evt.preventDefault) {
		evt.preventDefault();
	} else {
		evt.returnValue = false;
	}
}

/**
 * 获得[min, max)范围的随机整数
 * @param {Number} min
 * @param {Number} max
 */
function randomInt(min, max) {
	return parseInt(Math.random() * (max - min) + min);
}

/**
 * 获得随机颜色
 */
function randomColor() {
	var red = randomInt(0, 256);
	var green = randomInt(0, 256);
	var blue = randomInt(0, 256);
	return "rgb(" + red + "," + green + "," + blue + ")";
}

function createTable() {
	document.write("<table class='t99'>");
	for (var i = 1; i <= 9; i += 1) {
		document.write("<tr>");
		for (var j = 1; j <= i; j += 1) {
			document.write("<td>");
			document.write(i + "*" + j + "=" + i * j);
			document.write("</td>");
		}
		document.write("</tr>");
	}
	document.write("</table>");	
}
