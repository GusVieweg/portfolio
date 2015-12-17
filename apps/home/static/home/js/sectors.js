$(function() {

    // Utility Methods
    // ==============================================================================

    var degreesToRadians = function(degrees) {
        return Math.PI * degrees / 180;
    };

    var radiansToDegrees = function(radians) {
        return 180 * radians / Math.PI;
    };

    var modulo = function(value, mod) {
        return ((value % mod) + mod) % mod;
    };


    // Elements
    // ==============================================================================

    // The setting refers to the root SVG element that contains all the sectors.
    // Batch operations are not applied to the root though, in favor of application
    // to the sector group.
    var setting = $('#setting');

    // Refers to the topmost bar
    var breadcrumbs = $('#breadcrumbs');

    // The overlay serves as a opaque surface over the screen. This was initially designed
    // because it was anticipated that #content was going to be slightly opaque, and I did
    // not want to be able to see through the div. This is no longer the case, but is still
    // useful to keep for styling purposes (for example, a border)
    var overlay = $('#overlay');

    // @nav_list refers to the hamburger icon that appears when an overlay is opened. This
    // will allow for quicker transitions between pages (as opposed to returning home and
    // selecting another sector every time)
    var nav_list = $('#nav-list');

    // @breadcrumbs merely tells us what page we're currently on. As we advance throughout, we
    // continue to add to the breadcrumbs, which we'll eventually allow for navigation. This will
    // probably be placed into a separate file at some point, and we'll have to allow for application
    // of animations and subsequent reversals of those animations.
    var breadcrumbs = $('#breadcrumbs');


    // Sector Construction
    // ==============================================================================

    // Then number of sectors in the stage. @sector_padding
    // refers to the amount of space in between the arcs, measured in degrees
    var sector_count = fk_stage.scenes.length;
    var sector_padding = 3;

    // @inner_radius and @outer_radius refer to the positions of the
    // inner and outer arcs of the sectors respectively.
    var inner_radius = 12;
    var outer_radius = 36;

    // @sectors refers to the actual @Sector objects defined below. These in turn
    // contain a group of all the SVG contents. @sector_group is a group containing
    // the collective sum of all SVG components involved in the menu
    var sectors = [];
    var sector_group = fk_stage.paper.g();

    // Refers to the index of the sector that is currently in the topmost
    // position. This is important for maintaining which sectors to advance
    // to and from (since the @getSelectedSector returns the index of the
    // sector numerically from topmost with value 0 to the sector immediately
    // left of the topmost with index (@sector_count - 1); that is, the selected
    // index is not relative to the position in the @sectors array!)
    var top_target_index = fk_stage.active;         // Refers to index that is the "top"
    var topmost = top_target_index;                 // Index of current top sector

    // Note these coordinates are defined relative to the viewbox, which should be
    // defined on the menu as "viewbox='0 0 100 100'"
    var center_x = 0;
    var center_y = 100;

    // A measure of the arc length, in terms of radians (note that this measurement
    // is suitable relative to both the @inner_radius and @outer_radius)
    var radians = Math.PI * (180 - sector_count * sector_padding) / (90 * sector_count);

    // Maintains a continual rotation value of the @sector_group.
    // Otherwise, it may not rotate at all. We also make sure to match
    // the sector groups rotation with the initial rotation for proper orientation
    var rotation = (radians + degreesToRadians(sector_padding)) / 4;

    // The angle offset a sector should be generated from.
    // Note that all sectors will probably start at this value, and then the sectors @.content
    // will be rotated for an even circle.
    var start_angle = -Math.PI / 2 - radians / 2 - rotation;

    // When building sectors, we start at angle (pi/2 - radians/2) to ensure that the
    // topmost sector is centered on the screen. Otherwise, the user would be forced
    // to select a sector to initialize a consistent layout. Note we also need to create
    // separate sectors instead of just nesting circles and drawing outward rays for
    // mouse effects; I was unsure of how to do it otherwise

    var Sector = function(arc_length, start_angle, scene) {

        // All content added to the group for simultaneous transformations
        this.content = fk_stage.paper.g();

        // Coordinates
        // --------------------------------------------------
        // Find coordinates of our sector, starting at SE-most point
        // and rotating counterclockwise (if arc was drawn in topmost orientation)

        var points = [];

        +function() {

            var end_angle = start_angle + arc_length;
            var radii = [inner_radius, outer_radius, outer_radius, inner_radius];
            var angle = [start_angle, start_angle, end_angle, end_angle];

            for(var i = 0; i < 4; i++) {
                points.push({
                    x: center_x + radii[i] * Math.cos(angle[i]),
                    y: center_y + radii[i] * Math.sin(angle[i])
                });
            }

        }.bind(this)();


        // Construct Path
        // --------------------------------------------------
        // Here we actually draw out the sector and add color.

        +function() {

            // Convenience variables
            var ir_str = " " + inner_radius + " " + inner_radius + " ";
            var or_str = " " + outer_radius + " " + outer_radius + " ";
            var coordinates = function(point) {
                return " " + point['x'] + " " + point['y'] + " ";
            };

            // Path
            var outline = fk_stage.paper.path(
                "M" + coordinates(points[0]) +
                "L" + coordinates(points[1]) +
                "A" + or_str + ", 0, 0, 1," + coordinates(points[2]) +
                "L" + coordinates(points[3]) +
                "A" + ir_str + ", 0, 0, 0," + coordinates(points[0]) +
                "Z"
            ).attr({ fill: 'none', stroke: '#CCC', strokeWidth: 0.2 });

            // Color
            var color_bar = fk_stage.paper.path(
                "M" + coordinates(points[0]) +
                "A" + ir_str + ", 0, 0, 1," + coordinates(points[3])
            ).attr({ fill: 'none', stroke: scene.color, strokeWidth: 1 });

            // Title
            var title = fk_stage.paper.text(center_x, center_y, scene.title).attr({
                'font-family': 'fredoka',
                'font-size': '3pt',
                'stroke': '#CCCCCC',
                'strokeWidth': 0.4,
                'fill': '#222222'
            });

            title.attr({
                'x': center_x - (title.getBBox().width / 2),
                'y': center_y - outer_radius + (title.getBBox().height + 2),
                'transform': 'r' + (-radiansToDegrees(rotation)) + ', ' + center_x + ', ' + center_y
            })

            this.content.add(outline, color_bar, title);

        }.bind(this)();


        // Utility Functions
        // --------------------------------------------------

        this.inPath = function(pos) {
            var trans = this.getMatrix();
            var tmp = pos.matrixTransform(trans.inverse());
            return Snap.path.isPointInside(this.content[0], tmp.x, tmp.y);
        };

        this.rotate = function(theta) {
            var rotation = new Snap.Matrix().rotate(theta, center_x, center_y);
            this.content.transform(rotation);
            return this;
        };

        this.getMatrix = function() {
            var trans = setting[0].createSVGMatrix();
            for(var key in this.content.matrix) {
                if(this.content.matrix.hasOwnProperty(key)) {
                    trans[key] = this.content.matrix[key];
                }
            }
            return trans;
        };

    };


    // Rendering
    // ==============================================================================

    // When building these sectors, we want to actually build them from our given stage,
    // so that the sectors are always in alignment with the correct act.

    for(var i = 0; i < sector_count; i++) {
        var sector = new Sector(radians, start_angle, fk_stage.scenes[i]);
        sector.rotate(i * (2 * sector_padding + radiansToDegrees(radians)));
        sector_group.add(sector.content);
        sectors.push(sector);
    }


    // Functions
    // ==============================================================================

    // Determines which sector is currently active
    // Note we must take a given point in the coordinate system of our viewbox
    // and then transform it according to the inverse transformations of our groups
    //
    // In addition, as explained in the comments of @topmost, this does not return
    // the index of the selected sector in the @sectors array. Instead it returns
    // the index of the drawn sector relative to the menu; e.g. no matter which
    // sector is topmost, selecting it will always return top_target_index.

    var getSelectedSector = function(event) {

        var pos = setting[0].createSVGPoint();
        pos.x = event.clientX; pos.y = event.clientY;
        pos = pos.matrixTransform(event.target.getScreenCTM().inverse());
        for(var i = 0; i < sectors.length; i++) {
            if(sectors[i].inPath(pos)) {
                return modulo(i - top_target_index, sectors.length);
            }
        }

        return -1;
    };


    // Event Handling
    // ==============================================================================

    // The following transitions the given page to the page represented by the sector.
    // This includes the animation effects and the initial calls used to bootstrap
    // the AngularJS process needed for the rest of the call (unless returning back
    // to the menu).

    fk_stage.dispatcher.on('rotate-sectors', function(event, index) {

        var deferred = $.Deferred();

        if(index === 0) {
            deferred.resolve();
        } else {
            var left = index > sectors.length / 2;
            var direction = (left) ? 1 : -1;
            var delta = (left) ? sectors.length - index : index;
            var angle_delta = (2 * sector_padding) + (180 * radians / Math.PI);

            topmost = modulo(topmost - direction * delta, sectors.length);
            rotation += direction * delta * angle_delta;

            sector_group.animate({
                transform: "r" + rotation + ", " + center_x + ", " + center_y
            }, 1000, mina.easeinout, deferred.resolve);
        }

        return deferred.promise();
    });

    // Perhaps a bit misleading, the following function does not expand the sector itself, but
    // instead displays the corresponding page the sector is referencing as an overlay on the
    // screen. We say @expandSector since the overlay itself is expanding.

    fk_stage.dispatcher.on('expand-overlay', function(event, index) {

        // Add breadcrumbs, and display toggle menu; this allows for faster transition
        // between pages, as opposed to selecting home, selecting a sector, etc.
        nav_list.css('display', 'block');
        breadcrumbs.find('ul.title-area').append(
            $('<li>').text(fk_stage.scenes[index].title.toUpperCase())
        );

        // Fill Screen, and allow chaining
        return overlay.css({
            'top': "-" + breadcrumbs.css('border-bottom-width'),
            'bottom': 0,
            'display': 'block',
            'background-color': fk_stage.scenes[index].light_color,
            'border-top': '5px solid ' + fk_stage.scenes[index].color
        }).promise().then(function() {
            return overlay.velocity({ 'right': 0 }, 600).promise();
        });

    });

    // Shrink overlay when returning home. Subsequently clear state as well.
    // Simply reverses the process in @expand-overlay

    fk_stage.dispatcher.on('contract-overlay', function(event, index) {

        var deferred = $.Deferred();

        nav_list.css('display', 'none');
        overlay.velocity({ 'right': '100%' }, 600).promise().then(function() {
            overlay.css({ 'top': '50%', 'bottom': '50%' });
            breadcrumbs.find('ul.title-area li+li').remove();
            deferred.resolve();
        });

        return deferred.promise();
    });


    // Mouse Hovering
    // ==============================================================================

    // Performs all animations/tweaks when hovering the mouse over a sector.
    // This includes cursor changes, glow effects, etc.

    setting.mousemove(function(event) {
        var selected = getSelectedSector(event);
        if(selected > -1) {
            setting.css('cursor', 'pointer');
        } else {
            setting.css('cursor', 'auto');
        }
    });


    // Sector Selection
    // ==============================================================================

    // During this scrolling, note that @selected here refers to the index of the selected scene,
    // but the rotate-sectors method expects the index of the selected sector, which is always the
    // same depending on position. Thus, what we actually must pass to the rotation is the offsetted
    // value.

    fk_stage.dispatcher.on('scroll', function(event, selected) {
        fk_stage.dispatcher.triggerHandler('rotate-sectors', [selected - topmost])
                .then(function() { return fk_stage.dispatcher.triggerHandler('expand-overlay', [topmost]); })
                .then(function() {
                    fk_stage.scenes[topmost].boot();
                });
    });

    // Similarly, the selected sector returns a sector relative to the sectors position. Thus,
    // we must propagate the absolute sector id instead.

    setting.click(function(event) {
        var absolute = null;
        var selected = getSelectedSector(event);

        if(selected == 0) {
            absolute = topmost;
        } else if(selected == 1) {
            absolute = topmost + 1;
        } else if(selected == fk_stage.scenes.length - 1) {
            absolute = topmost - 1;
        }

        if(absolute !== null) {
            absolute = modulo(absolute, fk_stage.scenes.length);
            fk_stage.dispatcher.trigger('scroll', [absolute]);
        }
    });

    breadcrumbs.find('li:first').click(function() {
        new Promise(function(resolve, reject) {
            var pane = $('#content-pane');
            if(pane.length === 0) resolve();
            else pane.velocity({ 'opacity': 0 }, resolve);
        }).then(function() {
            return fk_stage.dispatcher.trigger('contract-overlay', [topmost]);
        }).then(function() {
            overlay.children().first().remove();
        });
    });

});