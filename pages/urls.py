from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:user_id>/results/', views.results, name='results'),
	
]