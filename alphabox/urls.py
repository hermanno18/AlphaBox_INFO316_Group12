from django.urls import path
from . import views
app_name = 'alphabox'
urlpatterns = [
    # Url for the website home
    path("", views.index , name="home"),

    # Urls for the dashboard
    path("dashboard/evolution", views.dashboard_evolution , name="dashboard_evolution"),
    path("dashboard/profile", views.dashboard_profile , name="dashboard_profile"),
    path("dashboard/program", views.dashboard_program , name="dashboard_program"),
    path("dashboard/friends", views.dashboard_friends , name="dashboard_friends"),
    path("dashboard/others", views.dashboard_others , name="dashboard_others"),

    # Urls for the games
    # - Urls for the first game : "guess Words"
    path("game/guessWords", views.guess_words , name="game_guessWords_home"),
    path("game/guessWords/settings", views.dashboard_others , name="game_guessWords_settings"),
    # Urls for the inscription
    path("compte/inscription",views.inscription,name="inscription"),
    path("compte/connexion",views.connexion,name="connexion"),
    path("/",views.deconnection,name="deconnection"),
    path("mesUtilisateur",views.BASE,name="utilisateur"),
]
