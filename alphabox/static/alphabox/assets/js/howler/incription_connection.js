function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');

    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

$("#inscription_call").on("click",event=>{
    
    event.preventDefault();
    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
               type: 'POST',
               data : $("#inscription_form").serialize(), 
               url :urlajax1, 
               headers: {'X-CSRFToken': csrfTokenValue},
            success:function(data){
                if (data['username']!=''){
                    $("#registerModal").modal('toggle')
                    document.getElementById("inscription_form").reset()
                    document.getElementById("idEnregistrement").textContent=data['username']
                    document.getElementById("idEnregistrement").disabled = true;
                    document.getElementById("idConnexion").textContent="Bienvenue"
                    document.getElementById("idConnexion").disabled = true;
                }
                else{
                    document.getElementById("inscription_erreur").textContent=data['inscriptionMessage']
                }  
            },
            erro:function(){

                console.log("Erreur")
            }    
    })
  })  
 
$("#connexion_call").on("click",event=>{
    event.preventDefault();
    let csrfTokenValue=document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
        type:'POST',
        data: $("#connexion_form").serialize(),
        url:urlajax2,
        headers:{'X-CSRFToken': csrfTokenValue},
        success:function(data){
            if (data['username']!='') {
                $("#connexionModal").modal('toggle')
                document.getElementById("connexion_form").reset()
                document.getElementById("idEnregistrement").textContent=data['username']
                document.getElementById("idEnregistrement").disabled = true;
                document.getElementById("idConnexion").textContent="Bon retour"
                document.getElementById("idConnexion").disabled = true;
            }
            else{
                document.getElementById("connexion_erreur").textContent=data["connexionMessage"]
            }
                
        },
        erro:function(){
            console.log("Erreur")
        }    
    });
 })

