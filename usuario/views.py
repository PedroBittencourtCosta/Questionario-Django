from django.shortcuts import render

# Create your views here.

class login():

    def sigin(request):
        return render(request, 'login_page.html')