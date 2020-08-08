 // Your web app's Firebase configuration
 var firebaseConfig = {
     apiKey: "AIzaSyBJAJuTKQW8hqqSRU81wooBgoJzwIjv2BE",
     authDomain: "blast-f5230.firebaseapp.com",
     databaseURL: "https://blast-f5230.firebaseio.com",
     projectId: "blast-f5230",
     storageBucket: "blast-f5230.appspot.com",
     messagingSenderId: "397083851067",
     appId: "1:397083851067:web:b8d401072cb5599bce5f1e"
 };
 // Initialize Firebase
 firebase.initializeApp(firebaseConfig);
 var db = firebase.firestore();
 var storage = firebase.storage();