// (function($) {
//     'use strict';


function postData() {

    const myApi = "https://cors-anywhere.herokuapp.com/https://hello-lee.herokuapp.com/optimize"
    fetch(myApi, {
            method: "POST",
            body: JSON.stringify(monthly_expenses),
            headers: { 'Content-Type': 'application/json' }

        })
        .then(res => console.log("Successiful", res))


    home_utility = document.getElementById("sliderHome");
    transportation = document.getElementById("sliderTransportation");
    shopping = document.getElementById("sliderShopping");
    personal = document.getElementById("sliderPersonal");
    restaurant = document.getElementById("sliderRestaurant");
    insurance = document.getElementById("sliderShield");
    entertainment = document.getElementById("sliderVideo");
    travel = document.getElementById("sliderTravel");
    health = document.getElementById("sliderHealth");
    maintenance = document.getElementById("sliderMaintenance");

    monthly_expenses = {
        monthly_home_utility_spend: home_utility,
        monthly_transportation_spend: transportation,
        monthly_shopping_groceries_spend: shopping,
        monthly_personal_family_care_spend: personal,
        monthly_restaurant_dinning_spend: restaurant,
        monthly_insurance_spend: insurance,
        monthly_entertainment_spend: entertainment,
        monthly_travel_spend: travel,
        monthly_health_spend: health,
        monthly_maintenance_spend: maintenance
    }





}



function loadChart() {



    const myApi = "https://cors-anywhere.herokuapp.com/https://hello-lee.herokuapp.com/optimize"
    async function getAPI(url) {
        const res = await fetch(url);
        var mydata = await res.json();
        console.log(mydata);
    }
    getAPI(myApi);

    entertainmentAmount = mydata.minimized_entertainment;






    //Doughnut Chart
    new Chart(document.getElementById("chartBudget"), {
        type: 'doughnut',
        data: {
            labels: ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"],
            datasets: [{
                // label: "Population (millions)",
                // backgroundColor: ["#357ffa", "#f7b11b", "#ff6c60", "#8663e1", "#08bf6f", "#357ffa", "#f7b11b", "#ff6c60", "#8663e1", "#08bf6f"],
                // backgroundColor: ["#17406D", "#074986", "#095397", "#0E6BC0", "#487ECA", "#7A99D2", "#98ADDA", "#B2C0E1", "#C7D1E9", "#DCF7BA"],
                backgroundColor: ["#6F2C91", "#40BADA", "#DF6D27", "#DDB726", "#0067B3", "#8FB73E", "#6F2C91", "#40BADA", "#DF6D27", "#DDB726", "#0067B3", ],
                data: [2478, 5267, 734, 784, 433, 2478, 5267, 734, 784, 433]
            }]
        },
        options: {
            legend: {
                display: false,
                labels: {
                    fontColor: '#5c6dc0',
                }
            },
            title: {
                display: false,
                text: 'Predicted world population (millions) in 2050'
            },
            plugins: {
                labels: [{
                        render: 'image',
                        images: [
                            { src: '/static/icons/Home.png', width: 32, height: 22 },
                            { src: '/static/icons/Home.png', width: 32, height: 22 },
                            { src: '/static/icons/Home.png', width: 32, height: 22 }
                        ]
                    },
                    {
                        render: 'value',
                        position: 'border',
                        fontColor: 'white',
                        textMargin: 4,
                        outsidePadding: 4,
                        fontSize: 12,
                        textShadow: true,
                        fontStyle: 'bold'
                    }
                ]
            }
        }
    });
}
// })(jQuery);