from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import DeveloperDocument
from dashboard.models import Notification
from .forms import DeveloperDocumentForm
from django.core.exceptions import ObjectDoesNotExist
from django_notification.local_settings import BASE_URL

"""=========================================
    Developer Document
========================================="""


def developer_document(request):
    if request.user.is_authenticated:
        queryset = DeveloperDocument.objects.all().distinct()
        query = request.GET.get('q')
        if query:
            # Using strip method to remove extra white space
            query = query.strip()
            queryset = DeveloperDocument.objects.filter(
                Q(title__icontains=query) |
                Q(title__istartswith=query) |
                Q(title__endswith=query) |
                Q(details__icontains=query) |
                Q(file_type__icontains=query)
            ).distinct()
        page = request.GET.get('page')
        paginator = Paginator(queryset, 10)  # 10 posts per page
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'object_list': posts,
            'page': page
        }
        return render(request, "developer/developer-document.html", context)
    else:
        messages.add_message(request, messages.WARNING, "Sorry currently you don't have permission to access this file")
        return redirect('dashboard')


def add_developer_document(request):
    if request.method == 'POST':
        form = DeveloperDocumentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            title = form.cleaned_data['title']
            form = form.save(commit=False)
            form.created_by = request.user
            form.updated_by = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, "Developer document successfully uploaded !")
            # Create a notification for the user
            notification_message = f'Created : {title}'
            try:
                # Set the appropriate link if needed
                link = BASE_URL + "developer-document/"
            except:
                link = None
            notification = Notification(user=request.user, message=notification_message, link=link)
            notification.save()
            return redirect('developer-document')
        else:
            messages.add_message(request, messages.WARNING, "This file is too large to be uploaded.")
            return render(request, "developer/add-developer-document.html", {'form': form})
    else:
        form = DeveloperDocumentForm()
    return render(request, "developer/add-developer-document.html", {'form': form})


def update_developer_document(request, id):
    obj = get_object_or_404(DeveloperDocument, pk=id)
    form = DeveloperDocumentForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form = form.save(commit=False)
        form.updated_by = request.user
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Developer document successfully updated')
        # Update the associated notification message
        try:
            notification = Notification.objects.get(user=request.user, message__contains=obj.title)
            notification.message = f'Updated : {obj.title}'
            notification.save()
        except ObjectDoesNotExist:
            # Create a new notification if it does not exist
            Notification.objects.create(user=request.user, message=f'Updated: {obj.title}')
        return redirect('developer-document')
    return render(request, "developer/update-developer-document.html", {'form': form})


def delete_developer_document(request, id):
    obj = get_object_or_404(DeveloperDocument, pk=id)
    context = {
        'obj': obj
    }
    if request.method == "POST":
        obj.delete()
        messages.add_message(request, messages.WARNING, "Successfully Delete account document !")
        return redirect('developer-document')
    return render(request, "developer/delete-developer-document.html", context)
