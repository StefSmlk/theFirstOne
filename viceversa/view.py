from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def revers(request):
	return render(request, 'reverse.html', {'value': 'key'})