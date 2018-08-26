var ticking = false;
window.addEventListener("scroll", function () {
    if (!ticking) {
        window.requestAnimationFrame(function () {
            let p;
            for (let x of document.querySelectorAll(".main h1")) {
                if (p && x.offsetTop > (window.scrollY + 10)) {
                    document.querySelectorAll(".side li a").forEach(li => {
                        if (li.hash === "#" + p.id) {
                            li.className = "actived";
                        } else
                            li.className = "";
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