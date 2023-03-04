from django.shortcuts import render
from django.core.mail import send_mail

from config import settings


# Create your views here.

def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('contactEmail')
        subject = request.POST.get('contactSubject')
        content = request.POST.get('contactMessage')

        send_mail(
            subject,
            content,
            settings.EMAIL_HOST_USER,
            [to]
        )
        return render(
            request,
            'index.html'
        )
    else:
        return render(
            request,
            'index.html'
        )

