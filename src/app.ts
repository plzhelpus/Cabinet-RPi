import * as firebase from "firebase";

import * as config from "./config";

firebase.initializeApp(config.firebase);

const database = firebase.database();
const rpiRef = database.ref("cabinets/" + config.RPi.id);

rpiRef.on("child_changed", (snapshot) => {
  if (snapshot !== null) {
    console.log(snapshot.key);
    console.log(snapshot.val());
  }
})
