function selectAll() {
    // alert("Select All");
    var elements = document.getElementsByClassName("platform-box");
    var i;
    for (i = 0; i < elements.length; i++) {
        elements[i].checked = !elements[i].checked;
        if(elements[i].value == 'reddit')
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


function post(){
    var json = {};
    var elements = document.getElementsByClassName("platform-box");
    var i;
    for (i = 0; i < elements.length; i++) {
        json[elements[i].value] = elements[i].checked;
    }
    json["message"] = document.getElementById("post-text").value;
    
    var file = (document.getElementById("post-file").files[0]);
    if(file){
        var name = makeid(7)+".png";
        var ref = storage.ref().child("posts/"+name);
        ref.put(file).then(function(snapshot) {
            console.log('Uploaded a blob or file!');
            json["pic"] = name;
        });
    }else json["pic"] = "";

    if(json["reddit"]){
        json["subject"] = document.getElementById("subject").value;
        json["subreddit"] = document.getElementById("subreddit").value;
    }
    //send post to backend
    console.log(json);
}

function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
 }

 

 function updateReddit(value){
    var root = document.getElementById('reddit-fields');
    if(value){
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
    }
    else{
        while (root.firstChild) {
            root.removeChild(root.lastChild);
        }
    }
 }