from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
	path('questionnaires/', views.questionnaires, name='questionnaires_list'),
	path('questionnaires/questions_in_questionnaire/<int:questionnaire_id>', views.questioninquestionnaire, name='questions_in_questionnaire'),
	path('questionnaires/questions_in_questionnaire//<int:question_id>/', views.detail, name='detail'),
	# path('results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)