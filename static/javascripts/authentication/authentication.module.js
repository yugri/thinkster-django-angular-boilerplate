(function () {
  'use strict';

  angular
    .module('posspa.authentication', [
      'posspa.authentication.controllers',
      'posspa.authentication.services'
    ]);

  angular
    .module('posspa.authentication.controllers', []);

  angular
    .module('posspa.authentication.services', ['ngCookies']);
})();
