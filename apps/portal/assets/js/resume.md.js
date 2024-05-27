
window.addEventListener("zero-md-rendered", (e) => {
    const $root = e.target.shadowRoot.querySelector(".markdown-body");
    var $width = $root.offsetWidth;
    if ($width > 800) {
        $width = 800;
    }

    $root.querySelectorAll("iframe").forEach(element => {
        element.setAttribute("width", $width.toString());
        element.setAttribute("height", ($width * 0.5625).toFixed(0));
    });
});
