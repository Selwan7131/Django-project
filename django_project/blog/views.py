from django.shortcuts import render

"""
    to handle the trafic from the home page of our blog 
    the function is taking a request argument 
    the return of the function is what we want the user to see when they are sent to this route
    the return is am HTTP response 
    we didn't map our URL pattern to this view function, to do this we create a new bot module in our blog directory
    called urls.py and in that file is where we will map the urls that we want to correspond to each view function 
"""
"""
    now I can return a rendered template instead of HTTP response 
"""


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
