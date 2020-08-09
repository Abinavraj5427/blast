var modal = document.getElementById("myModal");

function redditDataGetter(x, ctx1, ctx2) {
    redditPlot1([x[0]["net upvotes"], x[0]["total downvotes"],
        x[0]["total upvotes"], x[0]["total votes"]], ctx1);
    redditPlot2([x[0]["total upvotes"], x[0]["total downvotes"]], ctx2);
}
function redditPlot1(data, ctx) {
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Net Upvotes", "Downvotes", "Total Upvotes", "Total Votes"],
            datasets: [{
                label: '# of Votes',
                data: data,
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(117,235,54,0.2)',
                    'rgba(208,235,54,0.2)',
                    'rgba(166,54,235,0.2)'
                ],
                borderColor: [
                    'rgb(102,255,219, 1)',
                    'rgba(117,235,54,1)',
                    'rgb(208,235,54, 1)',
                    'rgb(166,54,235, 1)',
                ],
                borderWidth: 1.5
            }]
        },
        options: {
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}
function redditPlot2(data, ctx) {
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ["Upvotes", "Downvotes"],
            datasets: [{
                label: 'Percentage',
                data: data,
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                    'rgb(141,19,0)'
                ],
                borderColor: [
                    'rgb(102,255,219, 1)',
                    'rgb(255,30,0)'
                ],
                borderWidth: 1.5
            }]
        },
        options: {
            legend: {
                display: true
            },
        }
    });
}

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
                    
                    dataDict = showCurrentAnalytics();
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

let dataDict = [];
function showCurrentAnalytics(){
    modal.style.display = "block";
    var json = {}
    var e = document.getElementById("post-selection");
    var value = e.options[e.selectedIndex].value;
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            var email = user.email;
            json['email'] = email;
            json['datetime'] = value;
            fetch("http://127.0.0.1:5000/data", {
                    method: 'POST',
                    mode: 'cors',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(json)
                })
                .then(response => response.json())
                .then(data => {
                    var ctx1 = document.getElementById('plot1').getContext('2d');
                    var ctx2 = document.getElementById('plot2').getContext('2d');
                    redditDataGetter(data, ctx1, ctx2);

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
                    }
                    mc.appendChild(span);

                    var b = document.createElement("h3");
                    b.innerHTML = "Loading Complete";
                    mc.appendChild(b);

                    var msg = document.createElement('p');
                    msg.id = "post-message";
                    msg.innerHTML = "Graphs and Charts are ready.";
                    mc.appendChild(msg);
                });
        } else {
            // User is signed out.
            // ...
            window.location.href = "./index.html";
        }
    });
}

