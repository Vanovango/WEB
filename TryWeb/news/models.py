from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Пусто')
    anons = models.CharField('Анонс', max_length=250, default='Пусто')
    full_text = models.TextField('Статья', default=' ')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'