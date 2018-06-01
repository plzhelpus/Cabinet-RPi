import * as firebase from "firebase";
import * as five from "johnny-five";
import Raspi from "raspi-io";
import * as config from "./config";

const board = new five.Board({
    io: new Raspi(),
    repl: false,
});

board.on("ready", function() {
    firebase.initializeApp(config.firebase);

    const pin = "GPIO18";
    const servo = new five.Servo(pin);

    const database = firebase.database();
    const rpiRef = database.ref("cabinets/" + config.RPi.id);

    rpiRef.on("child_changed", (snapshot) => {
      if (snapshot !== null) {
        console.log(snapshot.key);
        console.log(snapshot.val());
        if (snapshot.val()) {
            servo.max();
        } else {
            servo.min();
        }
      }
    });
});
