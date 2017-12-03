angular.module('app.main', [])

.controller('MainCtrl', function($scope, $http) {
    $scope.response = "";
    $scope.model_file={};
    
    $scope.uploadFile = function() {
        console.log("$scope.img_file");
        console.log($scope.img_file);
        var fd = new FormData();
        //Take the first selected file
        fd.append("file", $scope.img_file);
        console.log(fd);
        $http({
                url: urlapi + 'predict',
                method: "POST",
                headers: {
                    "Content-Type": undefined
                },
                data: fd
            })
            .then(function(data) {
                    console.log("response: ");
                    console.log(data.data);
                    // response reaction
                    $scope.response= data.data.result;
                },
                function(response) { // optional
                    // failed
                    console.log(response);
                });
    };

    /*$scope.takePhoto = function() {
        alert("a");
        console.log("take photo");
        var options = {
                quality: 100,
                destinationType: Camera.DestinationType.DATA_URL,
                sourceType: Camera.sourceType,
                allowEdit: true,
                encodingType: Camera.EncodingType.PNG,
                targetWidth: 500,
                targetHeight: 500,
                popoverOptions: CameraPopoverOptions,
                saveToPhotoAlbum: false,
                correctOrientation:true
            };

            $cordovaCamera.getPicture(options).then(function(imageData) {
                //$scope.user.newAvatar = "data:image/jpeg;base64," + imageData;
                $scope.img.imgdata = "data:image/jpeg;base64," + imageData;
                $scope.img.img = imageData;
                }, function(err) {
                console.log(err);
            });
    };*/
})
.directive('fileModel', [
    '$parse',
    function($parse) {
        return {
            restrict: 'A',
            link: function(scope, element, attrs) {
                var model = $parse(attrs.fileModel);
                var modelSetter = model.assign;

                element.bind('change', function() {
                    scope.$apply(function() {
                        if (attrs.multiple) {
                            modelSetter(scope, element[0].files);
                        } else {
                            modelSetter(scope, element[0].files[0]);
                        }
                    });
                });
            }
        };
    }
]);
