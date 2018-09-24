var ticking = false;
window.addEventListener("scroll", function () {
    if (!ticking) {
        window.requestAnimationFrame(function () {
            let p;
            for (let x of document.querySelectorAll(".main h1")) {
                if (p && x.offsetTop > (window.scrollY + 10)) {
                    document.querySelectorAll(".side li a").forEach(li => {
                        if (li.hash === "#" + p.id) {
                            li.parentNode.classList.add("actived");
                        } else
                            li.parentNode.classList.remove("actived");
                    });
                    break;
                }
                p = x;
            }
            ticking = false;
        });
        ticking = true;
    }
})