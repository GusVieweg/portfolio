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