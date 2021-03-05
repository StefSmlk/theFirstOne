from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def revers(request):
	user_text = request.GET['text']
	num = len(user_text.split())
	return render(request, 'reverse.html', {'text': user_text, 'reversed_text': user_text[::-1], 'num': num})