from django.shortcuts import render

"""
    let's just pretend that we made a database call and got back this list of posts
    and we want to display these posts on our blog Homepage,
    so we can pass these posts into our template, just by passing an argument with 
    our data and we'll put our data into a dictionary  

"""
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    # we can pass this context here in as our third argument to our render function
    # the data will be passed into our template
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
