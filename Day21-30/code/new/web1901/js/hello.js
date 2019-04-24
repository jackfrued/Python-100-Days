function randomColor(opacity=1) {
	let r = parseInt(Math.random() * 256)
	let g = parseInt(Math.random() * 256)
	let b = parseInt(Math.random() * 256)
	return `rgba(${r}, ${g}, ${b}, ${opacity})`
}
