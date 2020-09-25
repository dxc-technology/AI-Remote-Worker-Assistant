function runOptimizer() {
    displaySliderValue();
    loadChart();
}

function show_hide() {
    var container = document.getElementById("budgetCalculator");
    if (container.style.display == "none") {
        container.style.display = "block";
    } else {
        container.style.display = "none";
    }
}

// function activate_categories() {
//     var tgCategories = document.getElementById("tgCategories");
//     var cbCategories = document.getElementsByName("category");
//     if (tgCategories.checked == true) {
//         cbCategories.checked = true;
//     } else {
//         cbCategories.checked = false;
//     }
// }

// function activateCategories() {
//     var tgCategory = document.getElementById("tgCategories");
//     if (tgCategory.checked == true) {
//         check()
//     } else if (tgCategory.checked == false) {
//         uncheck()
//     }
// }

document.getElementById("tgCategories").onclick = function() {
    var tgCategory = document.getElementById("tgCategories");
    if (tgCategory.checked == true) {
        check();
    } else if (tgCategory.checked == false) {
        uncheck()
    }
};

// function activateCategories() {
//     var tgCategory = document.getElementById("tgCategories");
//     if (tgCategory.checked == true) {
//         check()
//     } else if (tgCategory.checked == false) {
//         uncheck()
//     }
// }

function check() {
    document.getElementById("cb_home").checked = true;
    document.getElementById("cb_transportation").checked = true;
    document.getElementById("cb_shopping").checked = true;
    document.getElementById("cb_personal").checked = true;
    document.getElementById("cb_restaurant").checked = true;
    document.getElementById("cb_insurance").checked = true;
    document.getElementById("cb_entertainment").checked = true;
    document.getElementById("cb_travel").checked = true;
    document.getElementById("cb_health").checked = true;
    document.getElementById("cb_maintenance").checked = true;

    document.getElementById("budgetCalculator").style.display == "block"


    // document.getElementsByName("category").checked = true;


    // var cbCategory = document.getElementsByName("category");
    // // for (var i = 0; i < cbCategory.length; i++) {
    // //     inputs[i].checked = true;
    // cbCategory.checked = true;



}



// var inputs = document.querySelectorAll(".check3");
// for (var i = 0; i < inputs.length; i++) {
//     inputs[i].checked = true;
// }

function uncheck() {
    document.getElementById("cb_home").checked = false;
    document.getElementById("cb_transportation").checked = false;
    document.getElementById("cb_shopping").checked = false;
    document.getElementById("cb_personal").checked = false;
    document.getElementById("cb_restaurant").checked = false;
    document.getElementById("cb_insurance").checked = false;
    document.getElementById("cb_entertainment").checked = false;
    document.getElementById("cb_travel").checked = false;
    document.getElementById("cb_health").checked = false;
    document.getElementById("cb_maintenance").checked = false;
}

function saveCategory() {
    var vb = document.getElementsByName("category");
    var budget = document.getElementsByName("budgetCategory")

    for (var i = 0; i < vb.length; i++) {
        if (vb[i].checked == false) {
            budget[i].style.display = "none";
        } else {
            budget[i].style.display = "table-row";
        }
    }



}




// document.getElementById("tgCategories").onclick = function() {
//     var tgCategory = document.getElementById("tgCategories");
//     if (tgCategory.checked == true) {
//         check();
//     } else if (tgCategory.checked == false) {
//         uncheck()
//     }
// };


// document.getElementById("start") = function() {
//     var sliderAmount = document.getElementsByName("sliderAmount");
//     var labelAmount = document.getElementsByName("labelAmount");

//     for (var i = 0; i < sliderAmount.length; i++) {
//         budget = sliderAmount[i].val();
//         labelAmount[i].text = budget;
//     }
// }



// function displaySliderValues() {
//     val = document.getElementById("sliderHome").value;
//     document.getElementById("lbHome").innerText = val;
// }

function displaySliderValue() {
    var sliderAmount = document.getElementsByName("sliderAmount");
    var labelAmount = document.getElementsByName("lbAmount");

    for (var i = 0; i < sliderAmount.length; i++) {
        val = sliderAmount[i].value;
        labelAmount[i].innerText = val;

    }

    computeTotal();
}

function computeTotal() {
    var sliderAmount = document.getElementsByName("sliderAmount");
    var lbTotalAmount = document.getElementById("lbTotalAmount");
    var totalAmount = 0;

    for (var j = 0; j < sliderAmount.length; j++) {
        val = sliderAmount[j].value;
        totalAmount = parseInt(totalAmount) + parseInt(val);
    }
    lbTotalAmount.innerText = totalAmount;
}

// ar nums = ['100', '300', '400', '60', '40'];
// var num = 0;

// for (var i = 0; i < nums.length; i++) {
//     num = parseInt(num) + parseInt(nums[i]);
// }

// for(var i=0; i < nums.length; i++){            
//     num += parseInt(nums[i]);  
// }
// alert(num);


// $(document).ready(function() {
//     $("#inputPls").click(function() {
//         var incomeAmount = $("#inputIncome").val();
//         // var slider = document.getElementsByClassName(".js-range-slider");

//         // for (var i =0; i < slider.length; i++){
//         //     slider[i].minimum
//         // }

//         $(".js-range-slider").attr("max", incomeAmount);

//     });
// });



function setMaxSliderValue() {
    var incomeAmount = $("#inputIncome").val();
    alert(incomeAmount);

    // $(".span.irs-max").css({ "max": incomeAmount });

    // document.getElementById("sliderHome").attr = 900;
    // $("#sliderHome").attr("data-max", 900);

    $(".span.irs-max").val("500");

    var homeSlider = document.getElementById("sliderHome");
    homeSlider.createAttribute("data-min", "800");

    // $("#sliderHome").val("900")
    // $(".js-range-slider").ionRangeSlider({
    //     min: 100,
    //     max: 800
    // });

    // document.getElementsByClassName(".js-range-slider").property.max = 100;
}

// $("#inputPls").click(function() {
//     $("#sliderHome").attr("data-max", "500");
// });


// $("#inputPls").click(function() {
//     var incomeAmount = $("#inputIncome").val();
//     alert(incomeAmount);
//     // var slider = document.getElementsByClassName(".js-range-slider");

//     // for (var i =0; i < slider.length; i++){
//     //     slider[i].minimum
//     // }

//     // $(".js-range-slider").attr(".irs-max", incomeAmount);
//     // $(".irs-max").val(incomeAmount);

//     $(".js-range-slider").ionRangeSlider({
//         max: incomeAmount;
//     });

// });