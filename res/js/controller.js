var familia = angular.module('familia', ['familia.controller']);

familia.controller('Familiares', function ($scope) {
  $scope.family = [
    {'name': 'Valentino Volpato',
     'desc': 'Fast just got faster with Nexus S.'},
    {'name': 'Dante Volpato',
     'desc': ''},
    {'name': 'Valentina Volpato',
     'desc': 'The Next, Next Generation tablet.'}
  ];
});
