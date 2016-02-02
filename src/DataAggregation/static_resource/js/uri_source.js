var app_rest_url = "http://139.196.56.37:8091/rest/service";
app = angular.module('rest.api', ['ngResource'])

//服务注册
app.factory('Category', ['$resource',
  function($resource){
      return $resource(app_rest_url+'/category/:category_id.json', 
    		  { category_id:'@category_id'},
    		  { query: {method:'GET', params:{} ,isArray:false}
      });
  }]);

app.factory('Type', ['$resource',
  function($resource){
      return $resource(app_rest_url+'/type/:type_id.json', 
    		  {	type_id:'@type_id'}, 
    		  { query: {method:'GET', params:{}, isArray:false}
      });
  }]);

app.factory('Base', ['$resource',
  function($resource){
      return $resource(app_rest_url+'/base/:serve_id.json', 
    		  { serve_id:'@serve_id',},
    	  	  { query: {method:'GET', params:{}, isArray:false}
      });
  }]);

app.factory('ServeAPI', ['$resource',
  function($resource){
      return $resource(app_rest_url+'/api/:id.json', 
              { id:'@id',},
              { query: {method:'GET', params:{}, isArray:false}
         });
  }]);

app.factory('ServeReqDemo', ['$resource',
  function($resource){
     return $resource(app_rest_url+'/reqdemo/:id.json', 
              { id:'@id',},
              { query: {method:'GET', params:{}, isArray:false}
         });
	}]);

app.factory('ServeReqFields', [ '$resource', 
  function($resource) {
	 return $resource(app_rest_url + '/reqfield/:id.json', 
			{id : '@id',}, 
			{query : {method : 'GET',params : {},isArray : false}
		 });
	 }]);

app.factory('ServeRespDemo', ['$resource',
    function($resource){
      return $resource(app_rest_url+'/respdemo/:id.json', 
             { id:'@id',},
             { query: {method:'GET', params:{}, isArray:false}
         });
      }]);

app.factory('ServeRespFields', [ '$resource', function($resource) {
      return $resource(app_rest_url + '/respfield/:id.json', 
             {id : '@id',}, 
             {query : {method : 'GET',params : {},isArray : false}
         });
      }]);

app.factory('ServeError', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/errorcode/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);

app.factory('ServePrice', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/price/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);

app.factory('ServeSDKPack', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/sdkpack/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);

app.factory('ServeActivePack', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/activepack/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);

app.factory('InvokeDemo', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/invokedemo/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);

app.factory('HttpDemo', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/httpdemo/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);

app.factory('ServeUpgrade', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/upgrade/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);

app.factory('ServeContact', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/contact/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);

app.factory('ServeOthers', [ '$resource', function($resource) {
    return $resource(app_rest_url + '/others/:id.json', 
           {id : '@id',}, 
           {query : {method : 'GET',params : {},isArray : false}
       });
    }]);


app.factory('CommonProvice', [ '$resource', function($resource) {
    return $resource('/common/location/provinces/', {}, 
           {query : {method : 'GET',params : {},isArray : true}
       });
    }]);


app.factory('CommonCity', [ '$resource', function($resource) {
    return $resource('/common/location/:province/citys', 
           {province : '@province',}, 
           {query : {method : 'GET',params : {},isArray : true}
       });
    }]);


app.factory('CommonDistrict', [ '$resource', function($resource) {
    return $resource('/common/location/:city/districts', 
           {city : '@city',}, 
           {query : {method : 'GET',params : {},isArray : true}
       });
    }]);



/**分页组件**/
function paginized($scope,pageObj){
	$scope.previous_page = pageObj.previous_page;
	$scope.next_page = pageObj.next_page;
	$scope.current_page = pageObj.current_page;
	var ext_page_range = 3;
	// 页码范围，top后展3页，buttom前沿3页
	var page_counts = Math.ceil(pageObj.total_counts / pageObj.page_size);
	var topIndex = Math.min(parseInt(pageObj.current_page,10)+ext_page_range,page_counts);
	var buttomIndex = Math.max(parseInt(pageObj.current_page,10)-ext_page_range,1);
	if(pageObj.previous_page == null || pageObj.previous_page == "undifined"){
		buttomIndex = parseInt(pageObj.current_page,10);
	}
	if(pageObj.next_page == null || pageObj.next_page == "undifined"){
		topIndex = parseInt(pageObj.current_page,10);
	}
	
	pageObj.page_no_range = new Array();
	for(var i = 1 ; i <= topIndex && i >= buttomIndex ; i++ ){
		pageObj.page_no_range.push(i);
	}
	$scope.page_no_range = pageObj.page_no_range;
}
