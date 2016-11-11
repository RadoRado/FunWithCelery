import time
from celery import shared_task, chain, group

from django.contrib.auth.models import User

@shared_task
def start_here(*args, **kwargs):
    print(args)
    print(kwargs)

    return 42

@shared_task
def sleepy_task(seconds):
    time.sleep(seconds)

    return 42

@shared_task
def send_confirmation_email(user_id):
    user = User.objects.get(id=user_id)

    print('Sending confirmation email to {}'.format(user.email))

    return user_id

@shared_task
def sum(a, b):
    return a + b

@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)

    print('Sending welcome email to {}'.format(user.email))

    return user_id

@shared_task
def call_full_contact(user_id):
    user = User.objects.get(id=user_id)

    print('Calling full contact for {}'.format(user.email))
    time.sleep(4)
    print('Calling full contact for {} done'.format(user.email))

    return user_id

@shared_task
def scrape_github(user_id):
    user = User.objects.get(id=user_id)

    print('Scraping github for {}'.format(user.email))
    time.sleep(5)
    print('Scraping github for {} done'.format(user.email))

    return user_id


@shared_task
def new_student_workflow(user_id):
    """
    Send confirmation email, wait 5 seconds, send welcome to course email
    """

    tasks = group(chain(send_confirmation_email.s(user_id),
                        send_welcome_email.s().set(countdown=5)),
                  call_full_contact.si(user_id),
                  scrape_github.si(user_id))

    tasks()
