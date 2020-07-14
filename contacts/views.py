from django.shortcuts import render, redirect

# Create your views here.
def contacts(request):
	return render(request, 'contacts.html')

