$(document).ready(function() {
  $(".img-row").each(function() {
    var imgChildren = $(this).children().children();
    var minHeight = 1e6;
    $.each(imgChildren, function(index, value) {
      $(value).on("load", function() {
        var thisHeight = $(value).height();
        minHeight = Math.min(minHeight, thisHeight);
      });
    });
    $.each(imgChildren, function(index, value) {
      $(value).on("load", function() {
        $(value).height(minHeight);
      });
    });
  });
});

function setHeight(elems, minHeight) {
  $.each(elems, function(index, value) {
    $(value).height(minHeight)
  })
}