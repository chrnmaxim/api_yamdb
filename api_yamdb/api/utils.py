from django.core.mail import send_mail

from api_yamdb.settings import EMAIL_YAMDB


def send_confirmation_code(email, confirmation_code):
    """Sends confirmation code to user's email."""
    send_mail(
        subject='Код подтверждения',
        message=f'Ваш код подтверждения: {confirmation_code}',
        from_email=EMAIL_YAMDB,
        recipient_list=(email,),
        fail_silently=False,
    )
