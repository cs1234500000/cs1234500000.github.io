$(".header").click(function () {
    const $header = $(this);
    const $content = $header.next();
    
    $content.slideToggle(300, function () {
        $header.text($content.is(":visible") ? "Collapse" : "Expand");
    });

    // Add smooth transition for icon rotation
    $header.find('.icon').toggleClass('rotated');
});

// Add smooth scrolling to all links
$(document).ready(function() {
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 500, 'linear');
    });
});
