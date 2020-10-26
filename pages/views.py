from django.shortcuts import get_object_or_404, render
from polls.models import UserProfile

# Create your views here.
def index(request):
	return render(request, 'pages/index.html')

# display results
def results(request, user_id):
  user_raiting = get_object_or_404(UserProfile, pk=user_id)

  context = {
  	# 'question': question,
  	'user_raiting': user_raiting
  }
  return render(request, 'pages/results.html', context)
