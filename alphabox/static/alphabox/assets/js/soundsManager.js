/*
var myAudio = new Audio('static/temp/assets/sounds/_happy_clappy.mp3');
function playSound() {
    myAudio.play();
}
import {Howl, Howler} from 'howler';
const {Howl, Howler} = require('howler');

var sound = new Howl({
    src: ['sound.webm', 'static/temp/assets/sounds/_happy_clappy.mp3']
});
sound.play();
*/
var sound = new Howl({
    src: [SOUNDS_PATH+"_happy_clappy.mp3"],
    html5: true,
    loop: true,
    volume: 0.5,
    onend: function() {
      console.log('Finished!');
    },
    sprite: {
        home: [3000, 47000],
        laser: [4000, 1000],
        winner: [6000, 5000]
      }
});
state = 0;
function testson(){
    //    sound.play("laser");
    //    sound.play(); // pour jouer l'ensemble du fichier
    if(state == 0){
        sound.play('home');
        state = 1;
    }else{
        state = 0;
        sound.stop();
    }
}

