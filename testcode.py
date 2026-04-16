import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

django.setup()

from django.contrib.auth.models import User
from MainApp.models import Topic, Entry

topics = Topic.objects.all()
entries = Entry.objects.all()

print("***************** Printing Topics ***********")
for topic in topics:
    print(topic.id, topic, topic.text)


print("***************** Printing Users ***********")
for user in User.objects.all():
    print(user.id, user.username)
