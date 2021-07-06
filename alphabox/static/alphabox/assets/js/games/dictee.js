let valeurPrononcer="";
var sendword = true;
const msg2 = new SpeechSynthesisUtterance();
msg2.lang = 'en';
msg2.pitch = 0.75
msg2.rate =0.75
const speakButton2 = document.querySelector('#dictee');


function toggledictee(startOver = true) {
    speechSynthesis.cancel();
    
    if (sendword){
        if (startOver){
            valeurPrononcer = TABLEAU.random(TABLEAU.length)
            msg2.text = valeurPrononcer
        }
        sendword=false
    }
    speechSynthesis.speak(msg2);
}


$("#validWord").on("click", event => {
    if (!sendword){
        var word = document.getElementById("entryInput").value
        if (word == valeurPrononcer ) {
            displayTheAnswer(true, word)    
        }
        else{
            var reelAnswer = "The answer was :&nbsp; <b>" + valeurPrononcer+"</b>";
            displayTheAnswer(false,word)
            displayTheAnswer(true, reelAnswer, true) //on lui affiche la répose correcte
        }
        sendword=true
    }
})

speakButton2.addEventListener('click', toggledictee);