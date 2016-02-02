var app = angular.module('base_person_ng_app', ['rest.api']);

	//自定义变量绑定符号自定义
	app.config(function($interpolateProvider) {
		  $interpolateProvider.startSymbol('{[{');
		  $interpolateProvider.endSymbol('}]}');
		});
	
	
//	XXX.query().$promise.thenfunction(result){}); 可作为同步调用
	
	/**特别注意：  ng-controller 只能置于布局标签中，但对于input ，select ，button的组件标签的标签对内部添加ng-controller是无效的*/
	app.controller('locationController',
			function($scope, CommonProvice, CommonCity, CommonDistrict) {
				CommonProvice.query(function(results){
						$scope.provinces = results; 
					});
				$scope.provinceChange = function(province){
						if(province != null && province != ""){
							CommonCity.query({ province : province },function(results){
								$scope.citys = results;
							});
						}else{
							$scope.citys = [];
						}
				}
				$scope.cityChange = function(city){
						if(city != null && city != ""){
							CommonDistrict.query({ city : city },function(results){
								$scope.districts = results; 
							});
						}else{
							$scope.districts = [];
						}
				}
		});
	
