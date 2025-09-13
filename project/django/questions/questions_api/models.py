from django.db import models
from django.contrib.auth import get_user_model

class Questions(models.Model):
    
    text = models.TextField(verbose_name='Текcт вопроса', null=False, blank=False)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    
    class Meta:
        ordering = ['date_create']


class Answers(models.Model):
    
    user_id = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='user_answers_f', null=False)
    questions_id = models.ForeignKey(to=Questions, on_delete=models.CASCADE, related_name='questions_answers_f', null=False)
    text = models.TextField(verbose_name='Текст ответа', null=False, blank=False)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        ordering = ['date_create']