import * as config from "config";
import * as firebase from "firebase";

firebase.initializeApp(config.firebase);
console.log(config.firebase);

const database = firebase.database();

console.log(config.RPi.id);

const rootRef = database.ref();

rootRef.once("value").then((snapshot) => {
  console.log(snapshot.val());
}).catch((error) => {
  console.log(error);
});
