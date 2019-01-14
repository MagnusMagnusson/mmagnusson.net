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
    $('.ingredient-name-div input').bind('input', function () {
        addIngredientField();
        clearIngredientFields();
    });

    $("#new-step-button").on('click touchstart', function (e) {
        let li = $("<li></li>");
        let step_div_container = $('  <div class="step-div-container"></div>');
        let X = $('<div class="ex input-div">X</div>');
        let step_div = $('<div contenteditable="true" class="fake-input input-div step-div">');
        $(X).on('click touchstart', function (e) {
            $(li).detach();
        })
        $(step_div_container).append(X).append(step_div);
        $(li).append(step_div_container);
        $("#step-container ol").append(li);
    });
});

function addIngredientField() {
    let a = $("#ingredient-list-container ul li").last();
    let text = $(a).find(".ingredient-name-div input").val();
    if (text != "") {
        let li = $("<li></li>");
        let ingredientContainer = $(" <div class='ingredient-div'>");
        let amount = $('<div class="fake-input input-div amount-div"><input type="number" class="fill" /></div>');
        let unit = $('<div class="fake-input input-div unit-div"><input class="fill" type="text" /></div>');
        let ingredient = $('<div class="fake-input input-div ingredient-name-div"><input class="fill" type="text" /></div>');
        let X = $('<div class="ex input-div">X</div>')

        $(X).on('click touchstart', function () {
            $(li).detach();
        });

        $(ingredientContainer).append(amount).append(unit).append(ingredient).append(X);
        $(li).append(ingredientContainer);
        $("#ingredient-list-container ul").append(li);
        $('.ingredient-name-div input').bind('input', function () {
            addIngredientField();
        });
    }
}

function clearIngredientFields() {

}

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
			    window.location.href = "../hraefni/" + d.data.name;
			}
			else {
				console.log(d.error);
			}
		}
	});
}