(function () {
  'use strict';

  angular
    .module('posspa', [
      'posspa.config',
      'posspa.routes',
      'posspa.authentication',
      'posspa.layout',
      'ngMaterial'
    ]);

  angular
    .module('posspa.config', []);

  angular
    .module('posspa.routes', ['ngRoute']);

  angular
    .module('posspa')
    .run(run);

  run.$inject = ['$http'];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
