from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


"""
1. Написать модель в models.py
2. Провести миграции - отправить данные в БД
3. Добавить модель в админку (admin.py)
4. Сериализовать данные - написать сериализаторы к моделям
5. Написать вьюшки - функции для отображения данных/обработки запросов
6. Привязать в функциями пути/url

"""

class ToDo(models.Model):
    STATUSES = (
        ('NC', 'Not completed'),
        ('IP', 'In Progress'),
        ('D', 'Done')
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(
        verbose_name='Название',
        max_length=100
    ) #VARCHAR
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'задачи'
