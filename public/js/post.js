// Get the modal
var modal = document.getElementById("myModal");




function selectAll() {
    // alert("Select All");
    var elements = document.getElementsByClassName("platform-box");
    var i;
    for (i = 0; i < elements.length; i++) {
        elements[i].checked = !elements[i].checked;
        if (elements[i].value == 'reddit')
            updateReddit(elements[i].checked);
    }
    // elements.map(element => element.checked = true);
}

function onloadauth() {
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


function post() {
    modal.style.display = "block";
    var json = {};

    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            json['email'] = user.email;

            var elements = document.getElementsByClassName("platform-box");
            var i;
            for (i = 0; i < elements.length; i++) {
                json[elements[i].value] = elements[i].checked;
            }
            json["message"] = document.getElementById("post-text").value;

            var file = (document.getElementById("post-file").files[0]);
            if (file) {
                var name = makeid(7) + ".png";
                var ref = storage.ref().child("posts/" + name);
                ref.put(file).then(function (snapshot) {
                    console.log('Uploaded a blob or file!');
                    json["pic"] = name;
                });
            } else json["pic"] = "";

            if (json["reddit"]) {
                // console.log("REDDDDDDDDIT")
                json["subject"] = document.getElementById("subject").value;
                json["subreddit"] = document.getElementById("subreddit").value;
            }
            //send post to backend
            console.log(json);
            fetch("http://127.0.0.1:5000/post", {
                    method: 'POST',
                    mode: 'cors',
                    headers: {
                        'Content-Type': 'application/json',

                    },
                    body: JSON.stringify(json)
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);

                    var root = document.getElementById("mc");
                    while (root.firstChild) {
                        root.removeChild(root.lastChild);
                    }

                    // Get the <span> element that closes the modal
                    var mc = document.getElementById("mc");
                    var span = document.createElement("span");
                    span.className = "close";
                    span.innerHTML = "&times;";

                    // When the user clicks on <span> (x), close the modal
                    span.onclick = function () {
                        modal.style.display = "none";
                        window.location.href = "./post.html";
                    }
                    mc.appendChild(span);

                    var b = document.createElement("h3");
                    b.innerHTML = "Loading Complete";
                    mc.appendChild(b);

                    var msg = document.createElement('p');
                    msg.id = "post-message";
                    msg.innerHTML = "";
                    data.map(e => msg.innerHTML += "URL: " + e + "<br/>")
                    mc.appendChild(msg);
                });
        } else {
            window.location.href = "./index.html";
        }
    });

}

function makeid(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}



function updateReddit(value) {
    var root = document.getElementById('reddit-fields');
    if (value) {
        var div1 = document.createElement("div");
        div1.className = "cente-single form";
        var subject = document.createElement("input");
        subject.type = "text";
        subject.id = "subject";
        subject.placeholder = "Enter Post Title";
        var div2 = document.createElement("div");
        div2.className = "cente-single form";
        var subreddit = document.createElement("input");
        subreddit.type = "text";
        subreddit.id = "subreddit";
        subreddit.placeholder = "Subreddit ex. (r/memes)";
        div1.appendChild(subject);
        root.appendChild(div1);
        root.appendChild(document.createElement("br"));
        div2.appendChild(subreddit);
        root.appendChild(div2);
    } else {
        while (root.firstChild) {
            root.removeChild(root.lastChild);
        }
    }
}