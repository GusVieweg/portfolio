$(function() {

    // Borrowed from:
    // stackoverflow.com/questions/5560248/programmatically-lighten-or-darken-a-hex-color-or-rgb-and-blend-colors
    // Used on the @content div (nested in the @overlay) for an offset in color, which also allows
    // for a nice trim on the top by the @overlay div by merely offsetting the top absolute position

    var shadeBlend = function(p, c0, c1) {
        var n = p < 0 ? p * -1 : p;
        if(c0.length > 7) {
            var f = c0.split(",");
            var t = (c1 ? c1 : p < 0 ? "rgb(0,0,0)" : "rgb(255,255,255)").split(",");
            var R = parseInt(f[0].slice(4)), G = parseInt(f[1]), B = parseInt(f[2]);
            var r = Math.round((parseInt(t[0].slice(4)) - R) * n) + R;
            var g = Math.round((parseInt(t[1])-G) * n) + G;
            var b = Math.round((parseInt(t[2])-B) * n) + B;
            return "rgb(" + r + "," + g + "," + b +")";
        } else {
            var f = parseInt(c0.slice(1), 16);
            var t = parseInt((c1 ? c1 : p < 0 ? "#000000" : "#FFFFFF").slice(1), 16);
            var R1 = f >> 16, G1 = f >> 8 & 0x00FF, B1 = f&0x0000FF;
            var r = (Math.round(((t >> 16) - R1) * n) + R1) * 0x10000;
            var g = (Math.round(((t >> 8 & 0x00FF) - G1) * n) + G1) * 0x100;
            var b = Math.round(((t & 0x0000FF) - B1) * n) + B1;
            return "#" + (0x1000000 + r + g + b).toString(16).slice(1);
        }
    };


    // Scene
    // ==============================================================================

    /**
     * A scene is just a collection of attributes regarding the position, coloring, etc.
     * of the SVG elements on the screen. These are transitioned to and from by the stage,
     * according to events triggered by the user.
    */
    var Scene = function(id, options) {

        var s = $.extend({
            'title': 'N/A',
            'color': '#CCC',
            'angular-tag': 'div'
        }, options);

        // Basic Attributes
        this.id = id;
        this.title = s['title'];
        this.color = s['color'];
        this.light_color = shadeBlend(.75, this.color)

        // Angular used to compile new directives corresponding to the tag. That is, each scene has a
        // corresponding tag which generates a corresponding directive. This directive is then compiled,
        // which triggers the necessary pull requests to populate the page. Note the tag is not technically a
        // part of the scene; rather, it is used to bootstrap the next step following the scene selection.
        // See @window.fk_angular_bootstrap in the root-application.js file for further details.

        this.angular_tag = s['angular-tag'];
        this.boot = function() { fk_angular_bootstrap.trigger('boot', this.angular_tag); };

    };


    // Stage
    // ==============================================================================

    /**
     * The stage coordinates transitions between scenes, enabling an interactive experience
     * for the user when scrolling, changing pages, etc. All SVG elements are created beforehand,
     * and it is up to the stage to prepare the scene (by hiding certain elements, changing text/images,
     * etc.) for the transition.
    */
    var Stage = function(scenes) {

        // Setup
        // ------------------------------------------------------------------------------

        // Here we create the setup needed for all scenes; this provides proper coloring
        // to segment the sectors, dot scrolls, and icon tray from the content of the
        // given page.

        this.scenes = [];
        for(var i = 0; i < scenes.length; i++) {
            this.scenes.push(new Scene(i, scenes[i]));
        }

        this.paper = Snap(document.getElementById('setting'));
        this.paper.polygon([0, -100, 5, -100, 45, 100, 0, 100]).attr({ 'fill' : '#222', 'id': 'sidebar' });
        this.paper.line(5, -100, 45, 100).attr({ 'stroke': '#CCC' });


        // Event Dispatcher
        // ------------------------------------------------------------------------------

        // The following is used to connect all the components together; that is, events
        // are triggered by the dispatch and observers of the dispatch will respond
        // accordingly for synchronization purposes. For example, if I were to scroll down
        // the page, I would want the sectors to rotate accordingly.

        this.dispatcher = $({});

        // Test
        this.dispatcher.on('scene-transition', function(event, index) {
            $('body').css('background-color', this.scenes[index].scene_bg_color);
        }.bind(this));


        // Stage Selection
        // ------------------------------------------------------------------------------

        // The following determines which scene is currently active. This is the only place
        // @active should be modified.

        this.active = 1;
        this.dispatcher.on('scroll', function(event, selected) { this.active = selected; }.bind(this));


        // Sizing
        // ------------------------------------------------------------------------------

        // Since the SVG components aren't bound on the right side, we wrap a new div and force
        // the stage div to lie centered along the sidebar.

        $(window).resize(function() {
            var sidebar_width = $('#sidebar')[0].getBoundingClientRect().width;
            $('#stage').css('left', sidebar_width / 2 + 'px');
        }).trigger('resize');

    };


    // Initialization
    // ==============================================================================

    /**
     * The following global stage is the main workhorse of the application (or at least
     * the home page), enabling transitioning to different scenes. It is also used as
     * a repository on which the sectors are built from.
    */
    window.fk_stage = new Stage([
        {
            'title': 'Projects',
            'angular-tag': 'projects-pane',
            'color': '#859900'
        },
        {
            'title': 'About',
            'angular-tag': 'about-pane',
            'color': '#b58900'
        },
        {
            'title': 'Blog',
            'angular-tag': 'blog-pane',
            'color': '#6c71c4'
        },
        {
            'title': 'Resume',
            'angular-tag': 'resume-pane',
            'color': '#dc322f'
        },
        {
            'title': 'Share',
            'angular-tag': 'share-pane',
            'color': '#268bd2'
        },
        {
            'title': 'Subscribe',
            'angular-tag': 'subscribe-pane',
            'color': '#2aa198'
        }
    ]);

});

