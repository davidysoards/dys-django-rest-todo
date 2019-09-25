from django.db import models


class Task(models.Model):
    TODO = 0
    DONE = 1

    STATUS_CHOICES = (
        (TODO, 'To Do'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=TODO)
