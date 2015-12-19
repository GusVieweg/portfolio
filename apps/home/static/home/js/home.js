/**
 * Hero Unit
 * ===============================
 *
 * The following fills out the given canvas with a grid and randomly colors
 * certain blocks.
*/
$(function() {

    var hero = $('#hero');
    var canvas = hero.find('canvas');
    var context = canvas.get(0).getContext('2d');
    var context_width = parseInt(canvas.attr('width'), 10);
    var context_height = parseInt(canvas.attr('height'), 10);

    // Grid Properties
    var pixel_size = 4;
    var row_count = Math.ceil(context_height / pixel_size);
    var column_count = Math.ceil(context_width / pixel_size);

    // Draw Pixels
    for(var i = 0; i < column_count; i++) {
        for(var j = 0; j < row_count; j++) {
            if(Math.random() * column_count < 2) {
                context.fillStyle = '#00B9EB';
            } else {
                context.fillStyle = '#222222';
            }
            context.fillRect(i * pixel_size, j * pixel_size, pixel_size, pixel_size);
        }
    }

    // Draw Grid Lines
    context.beginPath();
    context.fillStyle = '#CCCCCC';
    for(var i = 0; i < row_count; i++) {
        context.moveTo(0, i * pixel_size);
        context.lineTo(context_width, i * pixel_size);
    }
    for(var i = 0; i < column_count; i++) {
        context.moveTo(i * pixel_size, 0);
        context.lineTo(i * pixel_size, context_height);
    }
    context.stroke();

});

/**
 * AngularJS Processing
 * ===============================
 *
 * I use Angular to load in the projects/blog/research panes.
*/
(function() {

    var app = angular.module('rootApplication', []);

    // This contains the content that will be switching back and forth
    app.controller("ContentController", ['$http', function($http) {
        var content = this;

        // Tabbing
        content.tab = 1;
        content.isSet = function(tab) { return content.tab == tab; }
        content.setTab = function(tab) { content.tab = tab; }

        // Projects
        content.projects = [];
        $http.get('projects/?format=json').success(function(data) {
            content.projects = data;
        });

    }]);



})();