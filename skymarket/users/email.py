from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from djoser.conf import settings
from templated_mail.mail import BaseEmailMessage


class PasswordResetEmail(BaseEmailMessage):
    """
    Custom class for sending a password reset email.
    """
    template_name = 'email/password_reset_email.html'

    def get_context_data(self):
        """
        Returns the context data for the email message.
        """
        # PasswordResetEmail can be deleted
        context = super().get_context_data()
        context['domain'] = 'localhost:3000'
        context['site_name'] = 'Skymarket'

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        return context
