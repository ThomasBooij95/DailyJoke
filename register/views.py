from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
# from joke.views import getContext, getComments, getJokeNumber, parse_refer
# Create your views here.

def parse_refer(url):
	split = url.split('/')
	return split[-1]

	
def register_view(request):

	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			print("FORM = VALID")
			form.save()
			return redirect("/")
		else:
			print("FORM = INVALID")
	else:
		form =RegisterForm()
		
	# context = getContext()

	url = request.META.get("HTTP_REFERER")
	refer = parse_refer(url)

	if refer == '':
		return redirect("/")
	elif refer == 'liked':
		return redirect('/liked')
	else:
		return redirect("/")

def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			print("FORM = VALID")
			form.save()
			return redirect("/")
		else:
			print("FORM = INVALID")
	else:
		form =AuthenticationForm()
		
	# context = getContext()

	url = request.META.get("HTTP_REFERER")
	refer = parse_refer(url)

	if refer == '':
		return redirect("/")
	elif refer == 'liked':
		return redirect('/liked')
	else:
		return redirect("/")



