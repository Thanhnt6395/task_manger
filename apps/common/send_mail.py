from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import os


def send_mail_active(token):
    subject = 'Welcome to TN'
    host = os.environ.get("HOST", default="http://localhost:8000/")
    content = {
        'href': f"{host}user/active?token={token}",
        'username': token.user.username,
    }
    html_content = render_to_string('ActiveMail.html', content)
    from_email = settings.EMAIL_HOST_USER
    to = [token.user.email, ]
    msg = EmailMultiAlternatives(subject, '', from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()