from django.shortcuts import render, redirect
from .models import Notification
from django.contrib import messages


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/dashboard.html', )
    else:
        messages.add_message(request, messages.WARNING, "Sorry currently you don't have permission to access this file")
        return redirect('home')


def notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user).order_by('-id')
        return render(request, 'dashboard/notifications.html', {'notifications': notifications})
    else:
        messages.add_message(request, messages.WARNING, "Sorry currently you don't have permission to access this file")
        return redirect('home')
