function mCheck () {
    var isVisible = $('#collapsibleNavbar').is( ":visible" );
    console.log(isVisible)
    if (isVisible != true) {
        $(".navbar").attr('style', 'background-color: white !important;');
    } else {
        $(".navbar").attr('style', 'background-color: transparent !important;');
    }
}

$(function nCheck() {
    if ($(window).width() < 768) {
        $(".navbar").attr('style', 'background-color: white !important;');
    }
})

$(function () {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $(".navbar").attr('style', 'background-color: white !important;');
        } else {
            $(".navbar").attr('style', 'background-color: transparent !important;');
        }
    });
});


function checkW () {
    if ($(window).width() < 768) {
        $("#fchoose").text("")
        console.log("hi")
     }
     else {
        $("#fchoose").text("Choose file")
     }
}