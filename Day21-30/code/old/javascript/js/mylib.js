function randomColor() {
	var r = parseInt(Math.random() * 128 + 128);
	var g = parseInt(Math.random() * 128 + 128);
	var b = parseInt(Math.random() * 128 + 128);
	return 'rgb(' + r + ', ' + g + ', ' + b + ')';
}