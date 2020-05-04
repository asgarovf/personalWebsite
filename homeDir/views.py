from django.shortcuts import render,redirect
from .forms import FeedbackForm
from django.contrib import messages
# Create your views here.

def homepage(request):
	template = 'homeDir/home.html'

	if request.method == "POST":
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			full_name = form.cleaned_data.get('full_name')
			messages.info(request, f'Thanks for feedback {full_name}!')
			return redirect('homepage')
	else:
		form = FeedbackForm()



	context = {
	'title': 'Home',
	'form': form,
	}
	return render(request,template,context)

def schedule(request):
	
	template = 'homeDir/schedule.html'

	context = {
	'title':'MySchedule'
	}

	return render(request,template,context)