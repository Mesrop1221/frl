from django.core.mail import EmailMessage
from django.conf import settings

def mail(name,surname,msg,email,phone):

	msg = f'անուն։{name},{email},հեռախոսահամար։{phone},ազգանուն։{surname},{msg}'

	mail = EmailMessage(
		'Բողոքների և առաջարկներ',
		msg,
		settings.EMAIL_HOST_USER,
		[settings.EMAIL_HOST_USER],
	)
	mail.fail_silently = False
	mail.send()