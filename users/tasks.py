from celery import shared_task
from django.core.mail import send_mail
from beast_sets.settings import EMAIL_HOST_USER, EMAIL_SEND_TO

@shared_task
def add(x, y):
    return x + y

@shared_task
def send_via_email(email, code):
    send_mail(
        "Confirm code",
        f"{code}",
        EMAIL_HOST_USER, 
        [email],
        fail_silently=False
    )
    return "ok"


@shared_task
def send_daily_report():
    send_mail(
        "REPORT",
        "U created many accs",
        EMAIL_HOST_USER,
        [EMAIL_SEND_TO],
        fail_silently=False,
    )   
    return "ok"