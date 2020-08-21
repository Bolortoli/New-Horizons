

$(window, document, undefined).ready(function() {

    $('input').blur(function() {
      var $this = $(this);
      if ($this.val())
        $this.addClass('used');
      else
        $this.removeClass('used');
    });
  
    var $ripples = $('.ripples');
  
    $ripples.on('click.Ripples', function(e) {
  
      var $this = $(this);
      var $offset = $this.parent().offset();
      var $circle = $this.find('.ripplesCircle');
  
      var x = e.pageX - $offset.left;
      var y = e.pageY - $offset.top;
  
      $circle.css({
        top: y + 'px',
        left: x + 'px'
      });
  
      $this.addClass('is-active');
  
    });
  
    $ripples.on('animationend webkitAnimationEnd mozAnimationEnd oanimationend MSAnimationEnd', function(e) {
        $(this).removeClass('is-active');
    });

  });
/*----------------------------SWIPER JS-----------------------------*/

var swiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    spaceBetween: 0,
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        type: 'fraction',
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

var getServiceSliderImgs = document.getElementById("getPictures");
var serviceSliderImgs = getServiceSliderImgs.getElementsByClassName("get-photos");
var miniImgsContainer = document.getElementById("miniImgContainer");


var swiper2 = new Swiper('.swiper-container-two', {
    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        // slideriin zurguudiig avaad jijig huvilbariin pagination helbereer ashiglav
        renderBullet: function (index, className) {

            var miniImgSource = serviceSliderImgs[index].getAttribute("src");
            return '<span class="' + className + '">' + '<img style="height: 10vh;margin: 0vw;object-fit: cover;border-radius: 3px;" src="' + miniImgSource + '">' + '</span>';
        },
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
})

/*----------------------------SWIPER JS END-----------------------------*/

/*----------------------------HOME JS-----------------------------*/




var controller = new ScrollMagic.Controller({
    globalSceneOptions: {
        duration: "13%"
    }
}); //Scroll magic library


var listOfFloor = document.getElementById("floorContainer").getElementsByTagName("li");
var unvisibleList = document.getElementById("unvisibleList");
var lengthOfFloorList = listOfFloor.length - 1; // Because selecting elements starts from index zero
var planPhotos = document.getElementById("planPhotosContainer").getElementsByTagName("img");
var lengthOfPlanPhotos = planPhotos.length - 1;
var floorPhotoInfo = document.getElementById("planPhotoInfo").getElementsByClassName("invisible-plan-photo-info");
var lengthOfPhotoInfo = floorPhotoInfo.length - 1;
for (let i = 0; i <= lengthOfPhotoInfo; i++) {
    // giving ids
    floorPhotoInfo[i].setAttribute("id", "floorPhotoInfo" + i + "");

}

for (let i = 0; i <= lengthOfPlanPhotos; i++) {
    // giving ids
    planPhotos[i].setAttribute("id", "planPhoto" + i + "");

}

for (let i = 0; i <= lengthOfFloorList; i++) {

    listOfFloor[i].setAttribute("id", "floorList" + i + "");

    /* Changes variable declaration unique,
    because we are using appendChild method */
    var noMeanThing;
    var divElements = noMeanThing + i;

    divElements = document.createElement("div");
    divElements.setAttribute("id", "selectFloorList" + i + "");
    // adding href attribute to li element for Onclick to scroll animation
    listOfFloor[i].onclick = function clickToActive() {
        var getListOfUnvisible = document.getElementById("selectFloorList" + i + "");
        getListOfUnvisible.scrollIntoView(false);
        document.href = getListOfUnvisible;
        var html = document.documentElement;
        // zaasan id ruu scrolldoj bhad davhar scrolldohguin tuld setTimeout ashiglav
        setTimeout(function () {
            html.scrollTop += window.innerHeight / 2;
        }, 450);
    }
    // listOfFloor[i].getElementsByTagName("a")[0].setAttribute("href", "#selectFloorList"+i+"");
    unvisibleList.appendChild(divElements);

    /*------SCROLLMAGIC LIBRARY------LOOPING THROUGH LI, MINIPLANPHOTO AND FLOORINFO TO GIVE IDS-----------------------*/

    new ScrollMagic.Scene({
            triggerElement: "#selectFloorList" + i + ""
        })
        .setClassToggle("#floorList" + i + "", "active-floor-list")
        .addTo(controller);

    new ScrollMagic.Scene({
            triggerElement: "#selectFloorList" + i + ""
        })
        .setClassToggle("#planPhoto" + i + "", "showPlanImage")
        .addTo(controller);


    new ScrollMagic.Scene({
            triggerElement: "#selectFloorList" + i + ""
        })
        .setClassToggle("#floorPhotoInfo" + i + "", "planPhotoInfo")
        .addTo(controller);

    /*----SCROLLMAGIC LIBRARY END-----------------------------*/
}
//               Onclick events
// show blured 360
function hideSendInformationForm() {
    document.getElementById("sendInformationForm").style.display = "none";
    
}

function showSendInformationForm() {
    document.getElementById("sendInformationForm").style.display = "grid";
}

function showPanaroma() {
    document.getElementById("bluredPanaroma").classList.toggle("removeBlur");
    var iframe = document.createElement("iframe");
    iframe.setAttribute("src", "/panaroma/");
    document.getElementById("panaromaSection").appendChild(iframe);
}

function closeFixedInfo() {
    document.getElementById("planPhotoInfo").style.display = "none";
}

function showFixedInfo() {
    document.getElementById("planPhotoInfo").style.display = "block";
}

function clickEffect(e) {
    e.classList.toggle("clickedEffect");
    var listOfMarkers = document.getElementById("listOfMarkers").getElementsByTagName("a")

    if (listOfMarkers[0].classList.contains("clickedEffect")) {
        mapStyles["show"].push({
            featureType: "poi.business",
            stylers: [{
                visibility: "on"
            }]
        }, )
    }
    console.log(mapStyles)

}

function showMobileNav() {
    document.getElementById("mobileNav").classList.toggle("showMobileNav");

}

/*----------------------------HOME JS END-----------------------------*/


function initMap() {
    var centering = {
        lat: 47.916086652367,
        lng: 106.92043322309473
    };
    var newHorizon = {
        lat: 47.91547196704302,
        lng: 106.9216999411583
    };

    var map = new google.maps.Map(
        document.getElementById('map'), {
            zoom: 17,
            center: centering,
        });

    var buildingDescription = '<h4 style="font-size: 1.5vh; margin: 0.1vw !important;padding: 0.1vw !important;">New Horizons</h2>'
    var infoWindow = new google.maps.InfoWindow({
        content: buildingDescription,
        position: newHorizon,
    });

    infoWindow.open(map);

    var marker = new google.maps.Marker({
        position: newHorizon,
        map: map,
        title: 'New Horizons',
    });
    marker.addListener('click', function () {
        infoWindow.open(map, marker);
    });

    map.setOptions({
        styles: mapStyles["show"]
    });



    document.getElementById("busStation").addEventListener("click", () => {
        document.getElementById("busStation").classList.toggle("clickedEffect");
        var listOfMarkers = document.getElementById("listOfMarkers").getElementsByTagName("a")

        if (listOfMarkers[0].classList.contains("clickedEffect")) {
            mapStyles["show"].push({
                featureType: "transit",
                stylers: [{
                    visibility: "on",
                    fontSize: "2em",
                }]
            }, )
        } else {
            mapStyles["show"].push({
                featureType: "transit",
                stylers: [{
                    visibility: "off",
                }]
            }, )
        }
        map.setOptions({
            styles:   mapStyles["show"],

        });
    });
    document.getElementById("government").addEventListener("click", () => {
        document.getElementById("government").classList.toggle("clickedEffect");
        var listOfMarkers = document.getElementById("listOfMarkers").getElementsByTagName("a")

        if (listOfMarkers[1].classList.contains("clickedEffect")) {
            mapStyles["show"].push({
                featureType: "poi.government",
                stylers: [{
                    visibility: "on"
                }]
            }, )
        } else {
            mapStyles["show"].push({
                featureType: "poi.government",
                stylers: [{
                    visibility: "off"
                }]
            }, )
        }
        map.setOptions({
            styles:   mapStyles["show"],

        });
    });
    document.getElementById("medical").addEventListener("click", () => {
        document.getElementById("medical").classList.toggle("clickedEffect");
        var listOfMarkers = document.getElementById("listOfMarkers").getElementsByTagName("a")

        if (listOfMarkers[2].classList.contains("clickedEffect")) {
            mapStyles["show"].push({
                featureType: "poi.medical",
                stylers: [{
                    visibility: "on"
                }]
            }, )
        } else {
            mapStyles["show"].push({
                featureType: "poi.medical",
                stylers: [{
                    visibility: "off"
                }]
            }, )
        }
        map.setOptions({
            styles:   mapStyles["show"],

        });
    });
    document.getElementById("business").addEventListener("click", () => {
        document.getElementById("business").classList.toggle("clickedEffect");
        var listOfMarkers = document.getElementById("listOfMarkers").getElementsByTagName("a")

        if (listOfMarkers[3].classList.contains("clickedEffect")) {
            mapStyles["show"].push({
                featureType: "poi.business",
                stylers: [{
                    visibility: "on"
                }]
            }, )
        } else {
            mapStyles["show"].push({
                featureType: "poi.business",
                stylers: [{
                    visibility: "off"
                }]
            }, )
        }
        map.setOptions({
            styles:   mapStyles["show"],

        });
    });



}




let mapStyles = {

    show: [
        {
            featureType: "poi",
            stylers: [{
                visibility: "off"
            }]
        },


        {
            featureType: "transit",
            stylers: [{
                visibility: "off"
            }]
        },
        {
            elementType: "geometry.fill",
            stylers: [{
                color: "#181818"
            }]
        },
        {
            elementType: "labels.text.stroke",
            stylers: [{
                color: "#242f3e"
            }]
        },
        {
            elementType: "labels.text.fill",
            stylers: [{
                color: "#746855"
            }]
        },
        {
            featureType: "administrative.locality",
            elementType: "labels.text.fill",
            stylers: [{
                color: "#d59563"
            }]
        },
        {
            featureType: "poi",
            elementType: "labels.text.fill",
            stylers: [{
                color: "#d59563"
            }]
        },
        {
            featureType: "poi.park",
            elementType: "geometry",
            stylers: [{
                color: "#263c3f"
            }]
        },
        {
            featureType: "poi.park",
            elementType: "labels.text.fill",
            stylers: [{
                color: "#6b9a76"
            }]
        },
        {
            featureType: "road",
            elementType: "geometry",
            stylers: [{
                color: "#38414e"
            }]
        },
        {
            featureType: "road",
            elementType: "geometry.stroke",
            stylers: [{
                color: "#212a37"
            }]
        },
        {
            featureType: "road",
            elementType: "labels.text.fill",
            stylers: [{
                color: "#9ca5b3"
            }]
        },
        {
            featureType: "road.highway",
            elementType: "geometry",
            stylers: [{
                color: "#746855"
            }]
        },
        {
            featureType: "road.highway",
            elementType: "geometry.stroke",
            stylers: [{
                color: "#1f2835"
            }]
        },
        {
            featureType: "road.highway",
            elementType: "labels.text.fill",
            stylers: [{
                color: "#f3d19c"
            }]
        },
        {
            featureType: "transit",
            elementType: "geometry",
            stylers: [{
                color: "#2f3948"
            }]
        },
        {
            featureType: "transit.station",
            elementType: "labels.text.fill",
            stylers: [{
                color: "#d59563"
            }]
        },
        {
            featureType: "water",
            elementType: "geometry",
            stylers: [{
                color: "#17263c"
            }]
        },
        {
            featureType: "water",
            elementType: "labels.text.fill",
            stylers: [{
                color: "#515c6d"
            }]
        },
        {
            featureType: "water",
            elementType: "labels.text.stroke",
            stylers: [{
                color: "#17263c"
            }]
        },



    ],

     
    


};
