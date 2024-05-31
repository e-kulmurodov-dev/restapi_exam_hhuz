# from celery import shared_task
#
# from celery import shared_task
# from django.core.mail import EmailMessage
# from django.shortcuts import redirect
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
#
# from .tokens import account_activation_token
#
#
# @shared_task
# def send_activation_email(user_id, domain):
#     from .models import CustomUser
#     user = CustomUser.objects.get(pk=user_id)
#     subject = 'Activate your account'
#     context = {
#         'user': user,
#         'domain': domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': account_activation_token.make_token(user),
#     }
#     message = context
#     email = EmailMessage(
#         subject,
#         message,
#         to=[user.email]
#     )
#
#     email.send()
#
#     return message