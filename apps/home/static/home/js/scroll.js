$(function() {

    // Scroll Indicators
    // ==============================================================================

    /**
     * The first thing we do is add circular indicators to the left side of the screen.
     * These maintain which scroll pane we are on, and will change if either it is selected,
     * a sector is selected, or the user manually scrolls vertically.
    */
    (function() {

        var scroll_indicator = $('#scroll-indicator');
        for(var i = 0; i < fk_stage.scenes.length; i++) {
            scroll_indicator.find('ul').append($('<li>'));
        }

        fk_stage.dispatcher.on('scroll', function(event, selected) {
            scroll_indicator.find('.active').css('border-color', '#CCC').removeClass('active');
            scroll_indicator.find('li').eq(selected).addClass('active')
                            .css('border-color', fk_stage.scenes[selected].color);
        }).trigger('scroll', [fk_stage.active]);

        scroll_indicator.find('li').click(function() {
            var index = $(this).index();
            fk_stage.dispatcher.trigger('scroll', [index]);
        });

    })();



});