from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ссылка на пользователя
    rating = models.PositiveIntegerField()  # Оценка от 1 до 5
    text = models.TextField()  # Текст отзыва
    date_created = models.DateTimeField(auto_now_add=True)  # Дата создания отзыва

    def __str__(self):
        return f"Review by {self.user.username} on {self.date_created}"
