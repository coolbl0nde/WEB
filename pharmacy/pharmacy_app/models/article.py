from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_description = models.CharField(max_length=200, null=True, blank=True)  # Поле для краткого содержания
    image = models.ImageField(upload_to='articles/')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']  # Сортировка статей по убыванию даты публикации

    def __str__(self):
        return self.title