

function save(){
    window.location.href = "./configure.html";
}

function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

var platform = getUrlVars()['platform'];
document.getElementById("platform").innerHTML = platform;