let valeurPrononcer="";
var sendword = true;
const msg2 = new SpeechSynthesisUtterance();
msg2.lang = 'en-US';
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
        var word = document.getElementById("entryInput").ariaValueText
        if (word == valeurPrononcer ) {
            displayTheAnswer(true, word)    
        }
        else{
            var reelAnswer = "correct word is ->" + valeurPrononcer;
            displayTheAnswer(false,word)
            displayTheAnswer(true,reelAnswer)
            $('#nbCorrect').html(parseInt($('#nbCorrect').html()) + -1)
        }
        sendword=true
    }
})

speakButton2.addEventListener('click', toggledictee);