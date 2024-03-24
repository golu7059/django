from django.shortcuts import render

def home(request):
    peoples = [
        {'name': 'Golu Kumar', 'age': 22},
        {'name': 'vishal Kumar Giri', 'age': 20},
        {'name': 'Priyanshu Kumar', 'age': 22},
        {'name': 'piriya singh', 'age': 16},
        {'name': 'gamer', 'age': 32},
        {'name': 'Ahmed singh lassi', 'age': 15},
    ]


    # We use context to send data from backend to render in HTML
    return render(request, 'home/index.html', context={'peoples': peoples } )

def about(request):
    return render(request,"home/about.html")


def contact(request):
    return render(request , "home/contact.html")