import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Pizza

pizzas=Pizza.objects.all()

for p in pizzas: 
    print(p.id,'',p)

p=Pizza.objects.get(id=1)
print(p.text)
print(p.date_added)

comments = p.comment_set.all()

for c in comments:
    print(c.text)


