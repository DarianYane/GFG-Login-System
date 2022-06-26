#Archivo relacionado al link para validar los email
"""
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_typeclass TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return (
            text_type(user.pk) + text_type(timestamp)

        )
generate_token = TokenGenerator()
"""