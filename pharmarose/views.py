from django.shortcuts import render


# main Views


def home(request):
    return render(request, 'home2.html', {})


def about(request):
    return render(request, 'about.html', {})
