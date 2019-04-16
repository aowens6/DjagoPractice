import os

from django.core.mail.message import EmailMessage

email = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')

print(email)
print(password)

