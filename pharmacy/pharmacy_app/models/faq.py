from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
