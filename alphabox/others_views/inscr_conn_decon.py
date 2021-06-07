from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from alphabox.models import *
import bcrypt

USERNAME=None

def BASE(request):
	utilisateurs=Utilisateur.objects.all()
	res=""
	for user in utilisateurs:
		res=res+" ::----:: "+(user.UserName)
	context= {'contenue_base': res}
	return render(request,'alphabox/includes/mybase.html',context)

def SamePassword(password,conformpassword):
	return True if password == conformpassword else False
		
def Indatabase(login):
	utilisateurs=Utilisateur.objects.all()
	for user in utilisateurs:
		if login ==user.UserName:
			return True

	return False		

def AccepteCondition(condition):
	return True if condition != None else False

def correctPassword(password):
	return True if len(password)>5 else False

def UserExit(login,password):
	utilisateurs=Utilisateur.objects.all()

	for user in utilisateurs:
		if  user.UserName==login and password==user.Password:
			# bcrypt.checkpw(password.encode('utf-8'),user.Password.encode('utf-8'))
			return True
	return False


def inscription(request):
	if request.method=='POST' and request.is_ajax():
		pseudo=request.POST.get('pseudo')
		mail=request.POST.get('mail')
		password=request.POST.get('password')
		conformpassword=request.POST.get('conformpassword')
		accepte=request.POST.get('accepte')

		if Indatabase(pseudo):
			return JsonResponse({'inscriptionMessage':"Ce nom d'utilisateur est deja utilisé",'type':'danger','username':''})

		elif  not AccepteCondition(accepte):
			return JsonResponse({'inscriptionMessage':"vous devez accepté  les conditions d'utilisateurs",'type':'danger','username':''}) 

		elif not SamePassword(password,conformpassword):
			return JsonResponse({'inscriptionMessage':'vos mots de passe  ne sont pas identique','type':'danger','username':''})
		
		elif not correctPassword(password):
			return JsonResponse({'inscriptionMessage':'entre un mot de passe superieur a 5 caracteres','type':'danger','username':''})

		else:
			#password= bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
			user=Utilisateur(UserName=pseudo,Email=mail,Password=password)
			user.save()
			request.session.set_expiry(0)
			request.session[pseudo]=pseudo
			USERNAME=pseudo
			return JsonResponse({'inscriptionMessage':'inscription avec succes','type':'success','username':pseudo})
	else:
		raise http404    


def  connexion(request):
	if request.method=='POST' and request.is_ajax():
		login=request.POST.get('login')
		password=request.POST.get('loginpassword')
		remember=request.POST.get('remember')

		if not UserExit(login,password):
			return JsonResponse({'connexionMessage':'login ou mot de passe incorrect','type':'danger','username':''})
		if login in request.session:
			return JsonResponse({'connexionMessage':'vous etes deja connecte','type':'danger','username':''})
		else:
			#request.session.set_expiry(0)		
			request.session[login]=login
			USERNAME=login
			if remember != None:
				if login in request.COOKIES:
					pass
				else:
					response=JsonResponse({'connexionMessage':'you have login','type':'true','username':login})
					response.set_cookie("login",login)
					return response	
			return JsonResponse({'connexionMessage':'you have login','type':'true','username':login})
	else:
		raise http404 


def deconnection(request):
	response =render(request,'alphabox/home/index.html') 
	response.delete_cookie("login")
	liste=[]
	for key in request.session.keys():
		liste.append(key)
		
	for key in liste:	
		del request.session[key]

	return response
	
