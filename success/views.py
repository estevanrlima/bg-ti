from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from bg.settings import EMAIL_HOST_USER
from home.views import calc_burnout, cal_suggestions_burnout


def index(request):
    
    image_url = 'https://raw.githubusercontent.com/estevanrlima/bgtreinamentos/main/logo%20BG%20treinamentos.png'

    if request.method == 'POST':
        user_email = request.POST['userEmail']
            
        pont_burnout = calc_burnout(request)
        pont_burnout_str= cal_suggestions_burnout(pont_burnout)

        subject = 'Devolutiva - BG Saúde - Burnout'
        html_content = render_to_string('home/burnout.html', {
            'pont_burnout_str': pont_burnout_str,
            'image_url': image_url,
        })

        # Create the plain text version of the email (optional)
        plain_message = strip_tags(html_content)

        send_mail(
            subject,
            plain_message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user_email],
            fail_silently=False,
            html_message=html_content
        )

    return render(request, 'success/index.html')