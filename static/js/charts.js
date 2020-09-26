// (function($) {
//     'use strict';






function loadChart() {

    fetch("https://hello-lee.herokuapp.com/optimize")
        .then(response => response.json())
        .then(data => {
            console.log("Data:", data)
        });


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