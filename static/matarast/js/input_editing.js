$(document).ready(function () {

	$(document).on('click', function (e) {
		$(".editing").removeClass("editing").addClass("input");
	});
	$("#submit").on('click', function (e) {
		submitIngredient();
	});
	$(".input").on('click', function (e) {
		e.stopPropagation();
		$(".editing").removeClass("editing").addClass("input");
		$(this).removeClass("input").addClass("editing");
	});
	$("#image_submit").on('click', function (e) {
		window.image = $("#image_button").val();
		$("#image img").attr("src", window.image);
	});
	$(".foodclass-box").on("click", function () {
		let name = $(this).attr("name");
		let dad = parents[name];
		for (let d of dad) {
			kids = children[d]
			let dElement = $(".foodclass-box[name='" + d + "']");
			$(dElement).prop("disabled", "");
			for(let k of kids) {
				let kElement = $(".foodclass-box[name='" + k + "']");
				if ($(kElement).prop("checked")) {
					$(dElement).prop("checked", "true");
					$(dElement).prop("disabled", "true");
				}
			}
		}
	});
});


function submitIngredient() {
	let data = {}
	data["description"] = $("#description").html();
	data["names"] = {};
	for(let n of $(".name")) {
		if ($(n).val()) {
			data["names"][$(n).attr("name")] = $(n).val();
		}
	}
	data["image"] = window.image;
	data["classes"] = [];
	for(let box of $(".foodclass-box")) {
		if ($(box).prop("checked")) {
			data["classes"].push($(box).attr("name"));
		}
	}
	data = { "data": JSON.stringify(data) };
	$.ajax({
		type: "POST",
		url: new_ingredient_api,
		dataType: 'json',
		data: data,
		success: function (d) {
			if (d.success) {
				console.log(d.error);
			}
			else {
				console.log(d.error);
			}
		}
	});
}