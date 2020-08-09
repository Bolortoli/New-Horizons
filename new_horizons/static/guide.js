/*-----------home1.html code------------------*/



document.querySelector(".guide-middle-line").addEventListener("mousedown", firstMousedown);
document.querySelector(".get-body-cursor").addEventListener("click", clickToMoveMiddleLine);
var homeOneImgContainerOne = document.querySelector(".home-img2-container");

function firstMousedown(e) {
    var prevX = e.clientX;
    window.addEventListener("mousemove", mousemove);
    window.addEventListener("mouseup", mouseup);

    function mousemove(e) {
        var containerWidth = homeOneImgContainerOne.getBoundingClientRect();
        homeOneImgContainerOne.style.width = containerWidth.width - (prevX - e.clientX) + "px";
        prevX = e.clientX;
    }

    function mouseup(e) {
        window.removeEventListener("mousemove", mousemove);
    }
}

function clickToMoveMiddleLine(e) {
    var getClientX = e.clientX;
    var containerWidth = homeOneImgContainerOne.getBoundingClientRect().width;
    var distanceOfMove = getClientX - containerWidth;
    var i = 0;
    var stopAnimationRight = setInterval(moveMiddleLineRight, 1);

    if (distanceOfMove < 0) {
        var intDistanceOfMove = Math.abs(distanceOfMove);
        var stopAnimationLeft = setInterval(moveMiddleLineLeft, 1)

        function moveMiddleLineLeft() {
            if (i >= intDistanceOfMove) {
                clearInterval(stopAnimationLeft);
            } else {
                i = i + 12;
                homeOneImgContainerOne.style.width = containerWidth - i + "px";
            }

        }
    }

    function moveMiddleLineRight() {
        if (i >= distanceOfMove) {
            clearInterval(stopAnimationRight);
        } else {

            i = i + 12;
            homeOneImgContainerOne.style.width = containerWidth + i + "px";
        }

    }




}

function showMobileNav() {
    document.getElementById("mobileNav").classList.toggle("showMobileNav");
    document.getElementById("menuBarIcon").classList.toggle("whiteMenuBar")

}



/*-----------home1.html code END------------------*/
