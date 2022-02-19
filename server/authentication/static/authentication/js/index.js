function addCSS(filename){
    var link = $('<link />', {
        rel: "stylesheet",
        href: filename
    });
    $('head').append(link);
}

addCSS("{% static 'css/styles.css' %}");