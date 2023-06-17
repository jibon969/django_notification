from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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


def delete_notifications(request, id):
    obj = get_object_or_404(Notification, pk=id)
    obj.delete()
    messages.add_message(request, messages.WARNING, "Successfully delete notification !")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

