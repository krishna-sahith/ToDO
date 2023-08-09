from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)  # New field for completion status

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'tasks'

