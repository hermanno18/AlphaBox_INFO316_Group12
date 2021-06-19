
function setGameParameters(){

    //          a - on insere donc ces infos dans l'objet GAME_SETTING........ o
    GAME_SETTING.lang = document.getElementById('gameLang').value
    GAME_SETTING.timer = document.getElementById('gameTimer').value
    //GAME_SETTING.lang =  document.getElementById('gameOthersMembers').value
    
    //          b - on charge l'animation pour sélectionner une lettre
    $('#countdownModal').modal('show');
    $('#countdownValue').html($('#virtualKeyBoard').html());
    document.getElementById('entryInput').disabled = false
}

function setGameLetter(letter){
//            a - on insere donc ces infos dans l'objet GAME_SETTING          
            GAME_SETTING.letter = letter
                $('#countdownValue').html("<div class='d-flex justify-content-center' ><i class='fas fa-cog fa-spin fa-6x'></i></div>")
            
//            on incrémente l'attibut tours 
            GAME_SETTING.turn ++
//            c - on envois une requette Ajax pour sauver ses réglages
            //début AJAX
            //on vide la liste des précedents mots recomendés
            $("#randomWordsList").html("")
            $.ajax({
                data: GAME_SETTING , // on récupere les données du formulaire
                type: 'GET', // on précise la methode
                url: urlAjax_Setting, //l'url vers laquelle AJAX doit diriger la requette
                async: false,
                // on success 
                success: function(response) { // si tout se passe bien NOTE: reponse contient la réponse obtenu de la requette
                    // alors on fait des choeses ici
                    console.log("réponse: %o", response.randomWords) // ca c'est la commande pour dumper un objet en console
                    for (let index = 0; index < response.randomWords.length; index++) {
                      const randWord = "<li class='m-0 p-1 list-group-item list-group-item-action list-group-item-success '>"+response.randomWords[index]+"</li>" ;
                      $("#randomWordsList").html($("#randomWordsList").html()+randWord)
                    }
                    if (GAME_SETTING.gameModule == "guesWords"  || MODULE =='listening' || MODULE =='writing'  ){
                       if(MODULE =='typing'){
                         set_learningWords_typing(response.randomWords)
                       }
                       if(MODULE =='prononciation'){
                        set_learningWords_prononciation(response.randomWords)

                       }
                       if(MODULE =='listening'){
                        set_learningWords_listening(response.randomWords)

                      }
                      if(MODULE =='writing'){
                        set_learningWords_writing(response.randomWords)

                      }
                    }
                    else if(GAME_SETTING.gameModule == "learningMeaning"){
                      set_learningMeaning(response.randomWords)
                    }else if(GAME_SETTING.gameModule == "usingWords"){
                      set_usingWords(response.randomWords)
                    }
                  },
                // on error
                error: function(response) { //sinon
                    //on réagi ici
                    console.log("the error returned: %o", 'incorrect')
                }
            });
            //fin AJAX
            $('#countdownValue').html("<div class='d-flex justify-content-center' ><i class='fas fa-cog fa-spin fa-6x'></i></div>")
  
//          puis je démarre le compte à rebour 
            // Set the date we're counting down to
            var countDownDate = new Date().getTime()+4000;
            // Update the count down every 1 second
            var x = setInterval(function() {

                // Get today's date and time
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = countDownDate - now;

                // Time calculations for days, hours, minutes and seconds
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // Display the result in the element with id="demo"
                
                HTML =  seconds + "s ";
                $('#countdownValue').html(HTML)
                // If the count down is finished, write some text
                if (distance < 1) {
                clearInterval(x);
                $('#countdownModal').modal('toggle');
                
                
                //on appelle le jeu proprement dit  
                game(MODULE)
            }
            }, 1000);

}

function game(sub_module){
    if(sub_module == 'typing' || sub_module == 'writing'){
      document.getElementById('entryInput').focus()
    }
    var countDownDate = new Date().getTime()+GAME_SETTING.timer*1000;
    var x = setInterval(function() {
      var now = new Date().getTime();
      var distance = countDownDate - now;
      var seconds = Math.floor(distance / 1000);
      displayTimer = seconds;
      if(seconds < 2*GAME_SETTING.timer/3){
        displayTimer = '<span class="text-warning"> '+seconds+' </span>'
      }
      if(seconds < GAME_SETTING.timer/3){
        displayTimer = '<span class="text-danger"> '+seconds+' </span>'
      }
      $('#timerDisplay').html(displayTimer)

      if (distance < 1) {
        // une requette AJAX ici pour savegarder l'etat des donnes en BD et récuperer les mots au hasards
          clearInterval(x);
          
          output = $("#timeOutModal").html()
          $('#countdownValue').html(output)
          $('#countdownModal').modal('toggle');
          if(sub_module == 'typing' || sub_module == 'writing'){
            document.getElementById('entryInput').disabled = true
          }
      }
  }, 1000);
}

function displayTheAnswer(word_is_correct, word){
    if(!word_is_correct){
      test = 'danger';
      icon = "times"
      $('#ndErrors').html(parseInt($('#ndErrors').html()) + 1)
    }else{
      test = 'success';
      icon = 'check'
      $('#nbCorrect').html(parseInt($('#nbCorrect').html()) + 1)
    }
    list_item = "<li class='m-0 p-1 list-group-item list-group-item-action list-group-item-"+test+" b d-flex justify-content-between align-items-center'>"
    list_item+= "<div class='d-flex justify-content-between align-items-center'>"
    list_item+= "<i class='fas fa-1x fa-"+icon+"-circle mr-1'></i>" +  word + "</div>"
    if(test=='success'){
        list_item+="<div class='bg-dark p-1 rounded-sm  ' >"
        list_item+="<span class='badge badge-warning badge-pill text-white animation fadeIn infinite'>1</span> <span class='text-warning'> points </span> </div>"            
    }
    list_item+="</li>"
    document.getElementById('liste').innerHTML = list_item +document.getElementById('liste').innerHTML
    document.getElementById('entryInput').value=""
}

function  testWord(word, givenWords){
    if(navigator.onLine){ // si l'acces à internet est établit

        if(word != " "){
          position = word.indexOf(GAME_SETTING.letter)
          if(position == 0){ // si le mot qu'il a entré commence par la lettre sélectionée, on par chercher dans le dictionnaire
            
            if(givenWords.indexOf(word) ==  (-1)){ //si le mot n'est pas deja écrit
                url_api ="https://api.dictionaryapi.dev/api/v2/entries/"+ GAME_SETTING.lang+"/"+word
                $.ajax({
                  data: {} , // on défini les données à envoyer
                  type: 'GET', // on précise la methode
                  url: url_api, //l'url vers laquelle AJAX doit diriger la requette
                  // on success 
                  success: function(response) { // si tout se passe bien NOTE: reponse contient la réponse obtenu de la requette
                    // alors on fait des choeses ici

                        displayTheAnswer(true, word)
                        givenWords[givenWords.lenght] = word
                        document.getElementById('ajaxTestWordsCible').value = word
                        
                  },
                  //au ca où on ne trouves pas
                  error: function (xhr, ajaxOptions, thrownError) {
                    if(xhr.status == 404) {
                    // some error
                      displayTheAnswer(false, word)
                    }
                    else if(xhr.status == 403) {
                    // another error
                    alert('désolé, nous rencontrons un probleme en interne ')
    
                    }
                    else if(xhr.status == 500) {
                    // another error
                      alert('erreur interne !')
                    }
                    else {
                    // default error
                    }
                  }
                });
            }else{ //si ayu contraire le mot est deja dans un tableau de mots
                displayTheAnswer(false, word)
                console.log("tu as deja entré ce moyt au paravent") // ca c'est la commande pour dumper un objet en console
                document.getElementById('ajaxTestWordsCible').value = ""
            }

          }else{ //sinon, on marque ce mot comme incorrect
            displayTheAnswer(false, word)
          }
        }

  }else{
    alert("Vous n'etes pas en ligne nous ne pouvons pas contacter nos serveurs, vérifieé votre connection internet")
  }
}
function set_learningWords_typing(){

}
function set_learningWords_prononciation(){
  
}
function set_learningWords_writing(){
  
}
function set_learningWords_listening(randomWords){
  //alert('ici on découvre des nouveaux mots ! cool non ')
}

function set_learningMeaning(randomWords){
  //alert('nous smomes dans le module pour apprendre le sens des mots')
}

function set_usingWords(randomWords){
  //alert('bon là on va juste faire des super phrases avec les mots !!!')
} 