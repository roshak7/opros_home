from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from datetime import datetime
import pytz
from .models import Question, Choice, Questionnaire, QuestionInQuestionnaire, UserProfile

#Get questionnaires and display them
def questionnaires(request):
	
	allquestionnarires = Questionnaire.objects.all()
	context = {
		'allquestionnarires' : allquestionnarires,
	}
	context['date'] = pytz.UTC.localize(datetime.now())
	return render (request, 'polls/questionnaires_list.html', context)

def questioninquestionnaire(request, questionnaire_id):
	questionnaires = get_object_or_404(Questionnaire, pk=questionnaire_id)
	questions_in_questionnaire = QuestionInQuestionnaire.objects.filter(questionnaire__id=questionnaires.id)
	context = {
		'questionnaires': questionnaires,
		'questions_in_questionnaire': questions_in_questionnaire,
	}
	return render(request, 'polls/questions_in_questionnaire.html', context)

# Get questions and display them
def index(request):
    allquestions = Question.objects.all()
    context = {
    	'allquestions': allquestions
    	}
    context['date'] = pytz.UTC.localize(datetime.now())
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Вопроса не существует")
  return render(request, 'polls/detail.html', { 'question': question })

# # display results
# def results(request, user_id):
#   # question = get_object_or_404(Question, pk=question_id)
#   user_raiting = get_object_or_404(UserProfile, pk=user_id)

#   context = {
#   	# 'question': question,
#   	'user_raiting': user_raiting
#   }
#   return render(request, 'pages/results.html', context)

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    user = request.user
    question = get_object_or_404(Question, pk=question_id)
    questionnaire_id = QuestionInQuestionnaire.objects.get(id=question_id).questionnaire.id
    questionnaires = get_object_or_404(Questionnaire, pk=questionnaire_id)
    users_profile = UserProfile.objects.filter(user=user)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        multiple_choice = question.choice_set.filter(id__in=request.POST.getlist('choice'))
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
        	'questionnaires': questionnaires,
        	'question': question,
        	'user': user,
        	'error_message': "Вы не сделали выбор.",
        }
        return render(request, 'polls/detail.html', context)
    else:
    	user_data = UserProfile.objects.all()
    	for i in user_data:
    		i.raiting += selected_choice.choice_weight
    		i.save()
    	# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    	return HttpResponseRedirect(reverse('polls:questions_in_questionnaire',args=(1,)))
        
        # return HttpResponseRedirect(reverse('pages:results'))