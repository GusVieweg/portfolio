(function() {

    /**
     * When a menu is selected, we need to be able to load the proper components
     * of AngularJS into the ng-app. We do this via the following delegate, which
     * loads in the correct element directive used to continue navigating the site.
     *
     * To properly bootstrap, call "fk_angular_bootstrap.trigger('boot', ['tag'])"
     * where tag corresponds to the element directives defined below. For example,
     * to load the projects page, we call:
     *
     * > fk_angular_bootstrap.trigger('boot', ['projects']);
    */
    window.fk_angular_bootstrap = $({});


    /**
     * The root applications primary purpose is to package all dependencies
     * together. There exists a corresponding application for each sector
     * in the given menu. These are all injected under the root application.
     * Upon exiting back to the menu, the content is cleared, and we return
     * back to our initial state.
    */
    var app = angular.module('rootApplication', [
        'blogApplication',
        'projectApplication'
    ]);


    /**
     * The following is triggered whenever the fk_angular_bootstrap object is
     * triggered. It simply loads in a given tag and compiles it for handoff
     * to the corresponding directive, all of which are defined below.
    */
    app.directive('rootPane', ['$compile', function($compile) {
        return {
            restrict: 'A',
            link: function(scope, element, attrs) {
                fk_angular_bootstrap.on('boot', function(event, tag) {
                    var overlay = angular.element(document.getElementById('overlay'));
                    overlay.html("<" + tag + "><div></div></" + tag + ">");
                    $compile(overlay.children().first())(scope.$new());
                });
            }
        };
    }]);

})();