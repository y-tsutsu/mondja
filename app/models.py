import datetime

from django.contrib.auth import models as usermodels
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(usermodels.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_color(self):
        n = hash(self)
        if n % 7 == 0:
            return 'red'
        elif n % 7 == 1:
            return 'purple'
        elif n % 7 == 2:
            return 'blue'
        elif n % 7 == 3:
            return 'cyan'
        elif n % 7 == 4:
            return 'green'
        elif n % 7 == 5:
            return 'yellow'
        else:
            return 'orange'

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Memo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(usermodels.User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_tags_str(self):
        return ' '.join([t.name for t in self.tags.all()])

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
