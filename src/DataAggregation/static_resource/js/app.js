var app = angular.module('base_ng_app', ['rest.api']);

	//自定义变量绑定符号自定义
	app.config(function($interpolateProvider) {
		  $interpolateProvider.startSymbol('{[{');
		  $interpolateProvider.endSymbol('}]}');
		});
	
	app.config( [ '$compileProvider',function( $compileProvider ) //设置编译安全协议,添加javascript和chrome-extension
	           {  $compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|javascript|ftp|mailto|chrome-extension):/); }])
	
	//自定义 if else 标签,(使用ng-if标签会 增加div导致html布局乱套)
	app.directive('if', function($parse, $compile){
	      var compile = function($element, $attrs){
	    	  	var cond = $parse($attrs.true);
	      		var link = function($scope, $ielement, $iattrs, $controller){
		          $scope.if_node = $compile($.trim($ielement.html()))($scope, angular.noop);
		          $ielement.empty();
		          var mark = $('<!-- IF/ELSE -->');
		          $element.before(mark);
		          $element.remove();
		   
		          $scope.$watch(function(scope){
		        	  if(cond(scope)){
		        		  mark.after($scope.if_node);
		        		  $scope.else_node.detach();
		        	  } else {
		        		  if($scope.else_node !== undefined){
		        			  mark.after($scope.else_node);
		        			  $scope.if_node.detach();
		        		  }
		        	  }
		          });
	      		}
	      		return link;
	      }
	   
	      return {	compile: compile,
	             	scope: true,
	             	restrict: 'E'}
	   });
	   
	app.directive('else', function($compile){
	     var compile = function($element, $attrs){
	    	 var link = function($scope, $ielement, $iattrs, $controller){
		         $scope.else_node = $compile($.trim($ielement.html()))($scope, angular.noop);
		         $element.remove();
	    	 }
	       return link;
	     }
	   
	    return { compile: compile,
	             restrict: 'E'}
	   });
	
	//自定义过滤器
	app.filter('substr',function(){
	    return function(inputStr,limit){
	        return inputStr.substring(0,limit)+"...";
	    }
	});
	
	app.filter('default',function(){
	    return function(inputStr,rtnStr){
	        return (inputStr == null || inputStr == "" || inputStr == "undefined")? rtnStr : inputStr
	    }
	});
	
	app.filter('dict',function(){
	    return function(inputStr,dictStr){
	    	dictObj = eval('(' + dictStr + ')');
	    	if(dictObj.hasOwnProperty(inputStr)){
	    		return dictObj[inputStr];
	    	}
	    }
	});
	
	app.filter('serve_applied',function(){
	    return function(serve_id,listString){
	    	 userServeIds = listString.split(",");
	    	 for( var i = 0 ; i < userServeIds.length ; i ++ ){
	    		 if (userServeIds[i] == serve_id){
	    			 return "已申请";
	    		 }
	    	 }
	    	 return "申请开通";
	    }
	});
	
	app.filter('previouspage',function(){
	    return function(inputPageNo){
	        return parseInt(inputPageNo,10) - 1;
	    }
	});
	
	app.filter('nextpage',function(){
	    return function(inputPageNo){
	    	return parseInt(inputPageNo,10) + 1;
	    }
	});
	
	app.filter('calculate_starpos',function(){
	    return function(scores){
	    	 starpos = 1;
	    	 while (scores > 1.5 && scores < 5){
	    	     scores = scores - 1;
	    	     starpos = starpos + 25;
	    	 }
	    	 return starpos;
	    }
	});
	
	app.controller('catetypebaseController',
		function($scope,$timeout,$http) {
		$http.get(app_rest_url+'/cate_type_base/?format=json&page_no=1&page_size=8').success(
				function(result){ 
					$scope.serve_cates = result.results; 
					$timeout(function(){
						$scope.$apply(serviceMenuLazyInit)
					});
			});
	}); 
	
//	Base.query().$promise.then(function(result){}); 可作为同步调用
	
	app.controller('hotServiceController',
			function($scope, Base) {
			Base.query({ordering:'-base_statistics__app_counts',page_no:'1',page_size:'6',recursion:'1'},function(result){
					$scope.hotServes = result.results; 
				});
		});
	
	app.controller('latestServesController',
			function($scope, Base) {
			Base.query({ordering:'-create_time',page_no:'1',page_size:'6',recursion:'1'},function(result){
					$scope.latestServes = result.results
				});
		}); 
	
	app.controller('apicateController',
			function($scope, Base, Category) {
			Base.query(function(result){
					$scope.serves_counts = result.count;
				});
			Category.query(function(cate_result){
					$scope.serve_cates = cate_result.results;
					angular.forEach(cate_result.results,function(data,index,array){
						Base.query({category_id:data.id},function(base_result){
							$scope.serve_cates[index].serve_count = base_result.count;
						});
					});
				});
		});
	
	app.controller('apilisttitleController',
			function($scope, Base, Category) {
				$scope.serve_cate = {};
				var category_id = $('#cateid').val();
				if(category_id == 0){
					Base.query(function(result){
						$scope.serve_cate = {category_name:"所有数据",serve_counts:result.count };
					});
				}else{
					Category.query({category_id:category_id},function(result){
						$scope.serve_cate.category_name = result.category_name;
					});
					Base.query({category_id:category_id},function(result){
						$scope.serve_cate.serve_counts = result.count;
					});
				}
		});
	
	app.controller('apilistController',
			function($scope, Base) {
				$scope.serves_list = {}
				var category_id = $('#cateid').val();
				var ordering_str = getOrder($('#sortid').val());
				var page_no = $('#pageno').val();
				var page_size = 10;
				if(category_id == 0){
					Base.query({ordering:ordering_str,page_no:page_no,page_size:page_size,recursion:2},function(result){
						$scope.serves_list = result.results;
						var pageObj = { previous_page : result.previous,
								next_page	  : result.next,
								current_page  : page_no,
								page_size	  : page_size,
								total_counts  : result.count}
						paginized($scope, pageObj);
					});
				}else{
					Base.query({category_id:category_id,ordering:ordering_str,page_no:page_no,page_size:page_size,recursion:2},function(result){
						$scope.serves_list = result.results;
						var pageObj = { previous_page : result.previous,
								next_page	  : result.next,
								current_page  : page_no,
								page_size	  : page_size,
								total_counts  : result.count}
						paginized($scope, pageObj);
					});
				}
		});
	
	app.controller('apiDetailController',
			function($scope, Base ) {
				$scope.serve = {};
				var serve_id = $('#serve_id').val();
				Base.query({serve_id:serve_id,recursion:2},function(result){
						$scope.serve = result;
					});
		});
	
	app.controller('apiDetailAPIController',
			function($scope, $timeout, Base, ServeAPI, ServeReqDemo, ServeReqFields, ServeRespDemo, ServeRespFields) {
				var serve_id = $('#serve_id').val();
				Base.query({serve_id:serve_id,recursion:2},function(result){
						$scope.serve = result;
					});
				ServeAPI.query({service:serve_id},function(result){
						if(result.count > 0){
							$scope.serveapi = result.results[0];
						}
					});
				ServeReqDemo.query({service:serve_id},function(result){
						if(result.count > 0){
							$scope.serve_reqdemo = result.results[0];
						}
					});
				ServeReqFields.query({service:serve_id, recursion:1 },function(result){
						if(result.count > 0){
							$scope.serve_reqfields = result.results;
						}
					});
				ServeRespDemo.query({service:serve_id},function(result){
						if(result.count > 0){
							$scope.serve_respdemos = result.results;
							$timeout(function(){
								$scope.$apply(prettyCode)
							});
						}
					});
				ServeRespFields.query({service:serve_id, recursion:1 },function(result){
						if(result.count > 0){
							$scope.serve_respfields = result.results;
						}
					});
		});
	
	app.controller('apiDetailErrorController',
			function($scope, ServeError ) {
				var serve_id = $('#serve_id').val();
				ServeError.query({service:serve_id,recursion:1 },function(result){
						var errorsList = [];
						if(result.count > 0){
							for(var index in result.results){
								var errorWrapper = getIncludedErrorWrap(errorsList,result.results[index])
								if(errorWrapper == null){
									errorWrapper = {}
									errorWrapper.wrap_errors = []
									errorWrapper.wrap_name = result.results[index].error_type.error_type_name;
									errorWrapper.wrap_errors.push(result.results[index]);
									errorsList.push(errorWrapper);
								}else{
									errorWrapper.wrap_errors.push(result.results[index]);
								}
							}
							$scope.serve_errors = errorsList;
						}
					});
		});

	function getIncludedErrorWrap(errorsList,errorEle){
		for(var index in errorsList){
			if(errorsList[index].wrap_name == errorEle.error_type.error_type_name){
				return errorsList[index];
			}
		}
		return null;
	}
	
	app.controller('apiDetailpricelimitController',
			function($scope, Base, ServePrice, ServeSDKPack, ServeActivePack ) {
				$scope.serve = {};
				var serve_id = $('#serve_id').val();
				Base.query({ serve_id:serve_id },function(result){
						$scope.serve = result;
				});
				ServePrice.query({ service:serve_id,recursion:1 },function(result){
					if(result.count > 0){
						$scope.serve_price = result.results[0];
					}
				});
				ServeSDKPack.query({ service:serve_id },function(result){
					if(result.count > 0){
						$scope.serve_sdkpack = result.results[0];
					}
				});
				ServeActivePack.query({ service:serve_id },function(result){
					if(result.count > 0){
						$scope.serve_actpacks = result.results;
					}
				});
		});
	
	app.controller('apiDetailDemoController',
			function($scope, InvokeDemo, HttpDemo ) {
				var serve_id = $('#serve_id').val();
				InvokeDemo.query({ service:serve_id,recursion:1 },function(result){
					if(result.count > 0){
						$scope.invoke_demos = result.results;
					}
				});
				HttpDemo.query(function(result){
					if(result.count > 0){
						$scope.http_demos = result.results;
					}
				});
		});
	
	app.controller('apiDetailUpgradeController',
			function($scope, ServeUpgrade ) {
				var serve_id = $('#serve_id').val();
				ServeUpgrade.query({ service:serve_id,ordering:"upgrade_time" },function(result){
					if(result.count > 0){
						$scope.upgrade_logs = result.results;
					}
				});
		});
	
	
	app.controller('apiDetailContactController',
			function($scope, ServeContact ) {
				var serve_id = $('#serve_id').val();
				ServeContact.query({ service:serve_id },function(result){
					if(result.count > 0){
						$scope.contact = result.results[0];
					}
				});
		});
	
	
	app.controller('pricelistController',
			function($scope, Base ) {
				Base.query({ recursion : 1 },function(result){
					if(result.count > 0){
						$scope.service_list = result.results;
					}
				});
		});
	
	
	/* 
	app.controller('httpController', 
		function($scope, Category, Type, Base){
			Category.query().$promise.then(function(result1){
					$scope.cates = result1.results;
					angular.forEach(result1.results,function(data1,index1,array1){
						Type.query({category:data1.id}).$promise.then(function(result2){
							 $scope.cates[index1].serve_types = result2.results;
							 angular.forEach(result2.results,function(data2,index2,array2){
								 Base.query({serve_type:data2.id}).$promise.then(function(result3){
									 $scope.cates[index1].serve_types[index2].serve_bases = result3.results;
								 });
							 });
						});
					});
			});
	});
	*/
