from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .models import SlideShow

def home(request):
    album = SlideShow.objects.get(pk = 1)

    return render(request, 'SnakeBreeder/home.html', {'album': album})

def contact(request):
    if request.method == "GET":
        return render(request, 'SnakeBreeder/contact.html')
    if request.method == "POST":
        name = request.POST['name']
        from_email = request.POST['email']
        subject = 'snake-breeder.com - nouveau message  ' + name + " <" + from_email + ">"
        comment = request.POST['comment']
        if name and from_email and comment:
            try:
                send_mail(subject, comment, from_email, ['info@snake-breeder.com',])
                messages.add_message(request, messages.SUCCESS, 'Votre message nous est bien parvenu. Nous vous répondrons dans les plus brefs délais.')
            except BadHeaderError:
                messages.add_message(request, messages.ERROR, 'Une erreur s\'est produite, veuillez réessayer.Si l\'erreur persiste, veuillez nous joindre à inf                                                                                                                                   o@coeur-de-siberie.ch.')
                return render(request, 'SnakeBreeder/contact.html')
        else:
            messages.add_message(request, messages.ERROR, 'Une erreur s\'est produite. Tous les champs sont obligatoires.')
            return render(request, 'SnakeBreeder/contact.html')
        return render(request, 'SnakeBreeder/contact.html')