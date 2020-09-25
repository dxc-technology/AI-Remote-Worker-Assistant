(function($) {
    'use strict';

    /* Default Range Slider */
    $("#demo_0").ionRangeSlider({

        min: 0,
        max: 100
    });

    $(".js-range-slider").ionRangeSlider({
        skin: 'round',
        // min: 0,
        // max: 800
    });

    /* Skins */
    $("#demo_6").ionRangeSlider();

    $("#demo_7").ionRangeSlider({
        skin: 'big'
    });

    $("#demo_8").ionRangeSlider({
        skin: 'modern'
    });

    $("#demo_9").ionRangeSlider({
        skin: 'sharp'
    });

    $("#demo_10").ionRangeSlider({
        skin: 'round'
    });

    $("#demo_11").ionRangeSlider({
        skin: 'square'
    });

})(jQuery);