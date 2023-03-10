const params = new URLSearchParams(window.location.search);
const linkId = params.get("id");
console.log(linkId);

if (linkId) {
	window.onload = function() {
	linkTop = document.getElementById(linkId).offsetTop + 100;
	window.scrollTo(0, linkTop);
	}
}