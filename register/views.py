from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate


def parse_refer(url):
	split = url.split('/')
	return split[-1]

	
def register_view(request):

	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			print("FORM = VALID")
			form.save()
			#Log user in automatically
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)

			return redirect("/")
		else:
			print("FORM = INVALID")
	else:
		form =RegistrationForm()
	
	return render(request, 'registration.html', {'form': form})

