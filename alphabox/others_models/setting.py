from django.db import models

# Create your models here.

class Seting(models.Model):
    
    gameLang = models.CharField(max_length=15)
    gameTimer = models.CharField(max_length=100)
    gameOthersMembers =  models.CharField(max_length=100)


class typePartie(models.Model):
	
	libelle = models.CharField(max_length = 100)
	timer = models.DateTimeField()	 
	noteMax = models.IntegerField()
	description = models.CharField(max_length = 100)	

class Dictionnaire(models.Model):
	
	idDict = models.IntegerField()
	langue = models.CharField(max_length = 15)
	localisation = models.CharField(max_length = 20)
	name = models.CharField(max_length = 20)



class Partie(models.Model):

	type_Partie = models.ForeignKey(typePartie, on_delete=models.CASCADE) #Pour definir une relation un à plusieurs
	dico = models.ForeignKey(Dictionnaire, on_delete=models.CASCADE) #Pour definir une relation un à plusieurs

	idPartie = models.IntegerField()
	score = models.IntegerField()
	datePartie = models.DateTimeField()
	etat = models.CharField(max_length = 20)
	nbParticipant = models.IntegerField()


class JDashboard(models.Model):

	nbMotTrouve = models.IntegerField()
	nbMotPrononce = models.IntegerField()
	bestNoteDictee = models.IntegerField()
	nbDefiGagne = models.IntegerField()
	nbPartieJouer = models.IntegerField()
	nbPartiefGagne = models.IntegerField()
	visibility = models.BooleanField()
	nbPoints = models.IntegerField()
	languesApprise = models.CharField(max_length = 100)




class Joueur(models.Model):
	"""
	Une classe joueur
	"""

	parties = models.ManyToManyField(Partie) #Pour definir une relation plusieurs à plusieurs
	j_Dashboard = models.OneToOneField(JDashboard, on_delete=models.CASCADE,primary_key=True,) #Pour definir une relation un à un 
	#joueur = models.OneToOneField(Joueur, on_delete=models.CASCADE,primary_key=True,) #Pour definir une relation un à un 

	username = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	inscriptDate = models.DateTimeField()
	jPoints = models.IntegerField()  



class Mot(models.Model):

	dico = models.ForeignKey(Dictionnaire, on_delete=models.CASCADE) #Pour definir une relation un à plusieurs
	
	libelle = models.CharField(max_length = 100)
	signification = models.CharField(max_length = 100)
	image = models.CharField(max_length = 100)
	sound = models.CharField(max_length = 100)
	antonymes = models.CharField(max_length = 100)
	synonymes = models.CharField(max_length = 100)

class LProgram(models.Model):

	joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE) #Pour definir une relation un à plusieurs
	dico = models.ForeignKey(Dictionnaire, on_delete=models.CASCADE) #Pour definir une relation un à plusieurs
	
	dateDebut = models.DateTimeField()
	dateFin = models.DateTimeField()
	titre = models.CharField(max_length = 20)
	nbMots = models.IntegerField()



class Defi(models.Model):

	idDefi = models.IntegerField()
	mise = models.IntegerField()
	dateDefi = models.DateTimeField()

class Tips(models.Model):

	joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE) #Pour definir une relation un à plusieurs
	type_Partie = models.ForeignKey(typePartie, on_delete=models.CASCADE) #Pour definir une relation un à plusieurs

	idTips = models.IntegerField()
	libelle = models.CharField(max_length = 100)
	description = models.CharField(max_length = 100)
	typeTips = models.CharField(max_length = 100)
	cout = models.IntegerField()

	





