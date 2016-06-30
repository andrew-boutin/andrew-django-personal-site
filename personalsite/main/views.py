from django.shortcuts import render
from django.conf import settings


def index(request):
    """Index view for the site - 'Landing Page'."""
    return render(request, 'main/index.html', {'debug': settings.DEBUG})


def pcbuild(request):
    """Page for pc build information."""
    return render(request, 'main/pcbuild.html')


def gamedev(request):
    """Page for video game development information."""
    return render(request, 'main/gamedev.html')


def keyboard(request):
    """Page for keyboard custom build."""
    return render(request, 'main/keyboard.html')


def devprojects(request):
    """Page for development project information."""
    return render(request, 'main/devprojects.html')

