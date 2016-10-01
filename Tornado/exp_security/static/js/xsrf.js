function getCookie(name) {
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}

jQuery.postJSON = function(url, data, callback) {
    data._xsrf = getCookie("_xsrf");
    jQuery.ajax({
        url: url,
        data: jQuery.param(data),
        dataType: "json",
        type: "POST",
        success: callback
    });
}
