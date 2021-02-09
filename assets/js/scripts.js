$(document).ready(function () {
    $("img").each(function (index) {
        $(this).wrap($('<a>', {
            href: $(this).attr("src")
        }).addClass("lightbox"));
    })
    const lightbox = GLightbox({
        selector: "lightbox",
        openEffect: "none",
        closeEffect: "none",
    });
    $('.btn-download').each(function () {
        this.setAttribute("download", this.getAttribute("href").split('/').pop())
    })
})