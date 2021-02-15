function initSyntaxHighlight() {
    let codeEditor = $('.code-editor');
    const codePatterns = [
        {
            name: 'num',
            match: /^(\.?\b[0-9.]+)/
        },
        {
            name: 'string',
            match: /^(['"][^'"\n]*['"])/
        },
        {
            name: 'construction',
            match: /^\b(if|for|until|while|else|elif|elseif|do|hast|break|return|def|function|continue|switch|in|case)\b/
        },
        {
            name: 'types',
            match: /^\b(int|bool|str|string|char|real|num|float|number|array|list|stack|queue|dict|matrix)\b/
        },
        {
            name: 'function-call',
            match: [/^([a-zA-Z_]+[\w]* *)\(/, '', '(']
        }
    ]
    var highlight = window.csHighlight;
    codeEditor.each(function () {
        $(this).before('<div class="code-view"></div>');
        let thisCE = this;
        thisCE.oldVal = "";
        $(this).on("keydown", function (e) {
            if (e.key == 'Tab') {
                e.preventDefault();
                var start = this.selectionStart;
                var end = this.selectionEnd;
                this.value = this.value.substring(0, start) + "    " + this.value.substring(end);
                this.selectionStart = this.selectionEnd = start + 4;
            }
        });

        function setTimer() {
            var currentVal = $(thisCE).val();
            setTimeout(function () {
                if (currentVal != thisCE.oldVal) {
                    $(thisCE).change();
                }
                setTimer();
            }, 500);
        }

        $(this).on("change keyup paste propertychange", function () {
            var currentVal = $(this).val();
            if (currentVal == this.oldVal) {
                return;
            }
            $(".code-view").html(currentVal.replace(/\n/g, '<br />').replace(/\t/g, '    '));
            thisCE.oldVal = currentVal;
            highlight({
                selector: ".code-view",
                patterns: codePatterns
            })
        });
        setTimer()
    })
    codeEditor.scroll(function () {
        let cv = $('.code-view');
        cv.scrollTop($(this).scrollTop());
        cv.scrollLeft($(this).scrollLeft());
    });
    $('.code-view').scroll(function () {
        let ce = $('.code-editor');
        ce.scrollTop($(this).scrollTop());
        ce.scrollLeft($(this).scrollLeft());
    });
}

function initImageLightbox() {
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
}


$(document).ready(function () {
    $('.btn-download').each(function () {
        this.setAttribute("download", this.getAttribute("href").split('/').pop())
    })
    initImageLightbox()
    initSyntaxHighlight();
})