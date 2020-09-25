// (function($) {
//     'use strict';

function loadChart() {
    //Doughnut Chart
    new Chart(document.getElementById("chartBudget"), {
        type: 'doughnut',
        data: {
            labels: ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"],
            datasets: [{
                // label: "Population (millions)",
                backgroundColor: ["#357ffa", "#f7b11b", "#ff6c60", "#8663e1", "#08bf6f", "#357ffa", "#f7b11b", "#ff6c60", "#8663e1", "#08bf6f"],
                // backgroundColor: ["#17406D", "#074986", "#095397", "#0E6BC0", "#487ECA", "#7A99D2", "#98ADDA", "#B2C0E1", "#C7D1E9", "#DCF7BA"],
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
                        render: 'label',
                        position: 'outside'
                    },
                    {
                        render: 'percentage'
                    }
                ]
            }
        }
    });
}
// })(jQuery);