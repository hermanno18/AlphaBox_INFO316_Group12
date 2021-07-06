Array.prototype.random = function (length) {
  return this[Math.floor((Math.random() * length))];
}

function getIndice(valeur, items) {

  for (var i = items.length - 1; i >= 0; i--) {
    if (items[i] == valeur) {
      return i
    }
  }
}

function resetValues() {
  document.getElementById("text1").textContent = TABLEAU.random(TABLEAU.length)
  document.getElementById("text2").textContent = TABLEAU.random(TABLEAU.length)
  document.getElementById("text3").textContent = TABLEAU.random(TABLEAU.length)
  document.getElementById("text4").textContent = TABLEAU.random(TABLEAU.length)
}

function setVoice() {
  msg.voice = voices.find(voice => voice.name === this.value);
  toggle();
}

function toggle(startOver = true) {
  speechSynthesis.cancel();
  if (startOver) {
    listingOne = true //indique que l'utulisateur a ecouter au moin une fois
    msg.text = document.querySelector("#" + valeur).textContent;
    speechSynthesis.speak(msg);
  }
}

function setOption() {
  console.log(this.name, this.value); // show rate and pitch values
  msg[this.name] = this.value;
}


  const msg = new SpeechSynthesisUtterance();
  msg.lang = 'en-US'
  msg.pitch = 0.8
  msg.rate = 0.8
  let voices = [];
  const speakButton = document.querySelector('#speak');
  let nombreTrouver = 0;
  var listingOne = false
  var items = ["text1", "text2", "text3", "text4"];
  valeur = items.random(items.length)
  indice = getIndice(valeur, items)


  $("#" + items[0]).on("click", event => {
    if (listingOne) {
      listingOne = false
      valeur = items.random(items.length)
      let v=document.getElementById("text1").textContent
      resetValues()
      if (items[0] == items[indice]) {
        nombreTrouver = nombreTrouver + 1
        displayTheAnswer(true,v)
      }
      else{
        displayTheAnswer(false,v)
      }
      indice = getIndice(valeur, items)
    }
  })

  $("#" + items[1]).on("click", event => {
    if (listingOne) {
      listingOne = false
      valeur = items.random(items.length)
      let v=document.getElementById("text2").textContent
      resetValues()
      if (items[1] == items[indice]) {
        nombreTrouver = nombreTrouver + 1
        displayTheAnswer(true,v)
      }
      else{
        displayTheAnswer(false,v)
      }
      indice = getIndice(valeur, items)
    }
  })

  $("#" + items[2]).on("click", event => {
    if (listingOne) {
      listingOne = false
      valeur = items.random(items.length)
      let v=document.getElementById("text3").textContent
      resetValues()
      if (items[2] == items[indice]) {
        nombreTrouver = nombreTrouver + 1
        displayTheAnswer(true,v)
      }
      else{
        displayTheAnswer(false,v)
      }
      
      indice = getIndice(valeur, items)
    }
  })

  $("#" + items[3]).on("click", event => {
    if (listingOne) {
      listingOne = false
      valeur = items.random(items.length)
      let v=document.getElementById("text4").textContent
      resetValues()
      if (items[3] == items[indice]) {
        nombreTrouver = nombreTrouver + 1
        displayTheAnswer(true,v)
      }
      else{
        displayTheAnswer(false,v)
      }
      indice = getIndice(valeur, items)
    }
  })

  speakButton.addEventListener('click', toggle);
  

