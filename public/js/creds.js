


function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

var platform = getUrlVars()['platform'];
document.getElementById("platform").innerHTML = platform;

function onloadauth(){
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            // User is signed in.
            //   var displayName = user.displayName;
            //   var email = user.email;
            //   var emailVerified = user.emailVerified;
            //   var photoURL = user.photoURL;
            //   var isAnonymous = user.isAnonymous;
            //   var uid = user.uid;
            //   var providerData = user.providerData;
            // ...
        } else {
            // User is signed out.
            // ...
            window.location.href = "./index.html";
        }
    });
}

onloadauth();

function save(){
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            var email = user.email;
            var platform = getUrlVars()['platform'];
            console.log(document.getElementById("username").value);
            var usernamekey = platform+".username";
            var passwordkey = platform+".password";
            var confkey = platform+".configured";
            var json = {};
            json[usernamekey] = document.getElementById("username").value;
            json[passwordkey] = document.getElementById("password").value;
            json[confkey] = true;
            db.collection("users").doc(email).update(json)
            .then(function() {
                console.log("Document successfully updated!");
                
                window.location.href = "./configure.html";
            });

        } else {
            // User is signed out.
            // ...
            window.location.href = "./index.html";
        }
    });
}