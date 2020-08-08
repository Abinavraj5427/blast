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

function loadPosts(){
    // Firebase Auth
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {

            var docRef = db.collection("users").doc(user.email);

            //Check if doc exists
            docRef.get().then(function (doc) {
                if (doc.exists) {
                    console.log("Document data:", doc.data());

                    var root = document.getElementById('post-selection');
                    
                    for(let i = 0; i< doc.data().posts.length; i++){
                        
                        let post = doc.data().posts[i];
                        // console.log(post)
                        let option = document.createElement('option');
                        option.setAttribute('data-index', i);
                        // console.log(i);
                        option.value = post.datetime;
                        option.innerHTML = post.datetime;
                        root.appendChild(option);
                    }
                } else {
                    // doc.data() will be undefined in this case
                    console.log("No such document!");
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

loadPosts();