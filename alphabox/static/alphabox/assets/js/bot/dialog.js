
POSSIBLE_QUESTIONS = [
    ["bonjour", "salut", "hey",'hello', 'bjr', 'hola', 'hi','slt'],
    ["comment tu vas","ca va bien",],
    ['aide', 'secour', 'jeu','jeux', 'jouer',"comment jouer"],
    ['deviner', "ecriture","prononcer"],
    ['aurevoir', "bye bye","bye"],
]
ANSWER = [
    ['oui bonjour', 'oui oui salut', 'merci bonjour'],
    ["Je vais bien merci et toi?","cool merci et toi?","je vais super bien \n et toi?","bof... je suis là \net toi?","Je suis à fond dans une partie sur Alphabox, je t'ajoute si tu veux \net toi?","ca va merci\n et toi?",],
    ["tu as besoin d'aide? tu peux <a href=''>contacter l'equipe de dévelioppement</a>", "tu as rencontré des difficultés? essaye de <a href=''>contacter l'equipe de développement</a> pour avoir de plus amplis explications", "humm... ce probleme me dépasse, il faut <a href=''>contacter l'equipe</a> ils vont regler ca"],
    ["tu voeux des astuces pour deviner les mots? j'suis fort à ca", "le mode deviner les mots est pour le moment le seul  qui est complet"],
    ["tu me laisse deja ? ok bonne journée","Hooo deja?? bon... à la prochaine", "houla ! j'avais encore beaucoup à te dire, essaie de revenir de que possible !", "j'espere que tu me laisse pour aller jouer!"],
]

function bot_answer(question){
    for (let index = 0; index < POSSIBLE_QUESTIONS.length; index++) {
        const choices = POSSIBLE_QUESTIONS[index];
        question_index = choices.indexOf(question)
        if(question_index != -1){
            return ANSWER[index][Math.floor(Math.random() * ANSWER[index].length)]
            
        }
    }
    return "j'ai pas bien compris, peux-tu reformuler, STP ? "
}