from .models import Notification


def notification_value(request):
    unread_notifications = Notification.objects.filter(user=request.user, read=False).count()
    four_unread_notifications = Notification.objects.filter(user=request.user, read=False).order_by('-created_at')[:4]
    context = {
        "unread_notifications": unread_notifications,
        "four_unread_notifications": four_unread_notifications

    }
    return context
