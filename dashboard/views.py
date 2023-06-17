from django.shortcuts import render, redirect
from .models import Notification
from django.contrib import messages


def home(request):
    return render(request, "dashboard/home.html")


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/dashboard.html', )
    else:
        messages.add_message(request, messages.WARNING, "Sorry currently you don't have permission to access this file")
        return redirect('belasea')


def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-id')
    return render(request, 'dashboard/notifications.html', {'notifications': notifications})
