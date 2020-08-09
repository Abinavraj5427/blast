function configure(platform) {
    window.location.href = "./creds.html?platform=" + platform;
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
            loadConfig(user.email)
            // ...
        } else {
            // User is signed out.
            // ...
            window.location.href = "./index.html";
        }
    });
}

onloadauth();

function loadConfig(email) {
    var emailRef = db.collection("users").doc(email);
    console.log(email)
    emailRef.get().then(function (doc) {
        if (doc.exists) {
            console.log("Document data:", doc.data());
            document.getElementById("reddit-status").innerHTML = doc.data().reddit.configured ? "Configured" : "Not Configured";
            document.getElementById("twitter-status").innerHTML = doc.data().twitter.configured ? "Configured" : "Not Configured";
            document.getElementById("instagram-status").innerHTML = doc.data().instagram.configured ? "Configured" : "Not Configured";
            document.getElementById("facebook-status").innerHTML = doc.data().facebook.configured ? "Configured" : "Not Configured";
        } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
        }
    }).catch(function (error) {
        console.log("Error getting document:", error);
    });
}
firstTime();
function firstTime() {

    // Firebase Auth
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {

            var docRef = db.collection("users").doc(user.email);

            //Check if doc exists
            docRef.get().then(function (doc) {
                if (doc.exists) {
                    console.log("Document data:", doc.data());
                } else {
                    // doc.data() will be undefined in this case
                    console.log("No such document!");

                    //Create Record
                    db.collection("users").doc(user.email).set({
                            facebook: {
                                configured: false,
                                password: "",
                                username: ""
                            },
                            instagram: {
                                configured: false,
                                password: "",
                                username: ""
                            },
                            reddit: {
                                configured: false,
                                password: "",
                                username: ""
                            },
                            twitter: {
                                configured: false,
                                password: "",
                                username: ""
                            },
                            posts: []

                        })
                        .then(function () {
                            console.log("Document successfully written!");
                        })
                        .catch(function (error) {
                            console.error("Error writing document: ", error);
                        });
                }
            }).catch(function (error) {
                console.log("Error getting document:", error);
            });
            // ...
        } else {
            // User is signed out.
            // ...
            window.location.href = "./index.html";
        }
    });

}