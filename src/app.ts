import * as config from './config';
import * as firebase from 'firebase';

firebase.initializeApp(config.firebase);
console.log(config.firebase);

const database = firebase.database();

console.log(config.RPi.id);

const rootRef = database.ref();

rootRef.once("value").then(function (snapshot) {
  console.log(snapshot.val());
}).catch(function (error) {
  console.log(error);
});
