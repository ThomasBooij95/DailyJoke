from django.shortcuts import render

# Create your views here.


def joke_view(request):
	

	context = {}
	return render(request,'joke_template.html',context)
