function initImageLightbox() {
    $("img").each(function (index) {
        let style = "lightbox";
        if ($(this).attr("src").endsWith("gif")) {
            style += " gif-image"
        }
        $(this).wrap($('<a>', {
            href: $(this).attr("src")
        }).addClass(style));
    })
    const lightbox = GLightbox({
        selector: "lightbox",
        openEffect: "none",
        closeEffect: "none",
    });
}


$(document).ready(function () {
    $('.btn-download').each(function () {
        this.setAttribute("download", this.getAttribute("href").split('/').pop())
    })
    initImageLightbox()
})