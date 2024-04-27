from django.db import models


class TgUser(models.Model):
    tg_id = models.IntegerField(blank=False, null=False, verbose_name='Telegram Id')
    first_name = models.CharField(blank=True, null=True, max_length=256, verbose_name='Имя')
    last_name = models.CharField(blank=True, null=True, max_length=256, verbose_name='Фамилия')

    class Meta():
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Question(models.Model):
    text = models.CharField(blank=False, null=False, max_length=256, verbose_name='Вопрос')
    is_active = models.BooleanField(blank=False, null=False, default=False, verbose_name='Активен')

    class Meta():
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'

    def __str__(self) -> str:
        return self.text[:50] + '...'

class Course(models.Model):
    name = models.CharField(blank=False, null=False, max_length=256, verbose_name='Название')

    class Meta():
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'

    def __str__(self) -> str:
        return self.name

class Answer(models.Model):
    user = models.ForeignKey(TgUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.CharField(blank=False, null=False, max_length=256, verbose_name='Ответ')
    is_relevant = models.IntegerField(blank=True, null=True, verbose_name='is_relevant')
    object = models.IntegerField(blank=True, null=True, verbose_name='object')
    is_positive = models.IntegerField(blank=True, null=True, verbose_name='is_positive')

    class Meta():
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'

    def __str__(self) -> str:
        return self.text[:50] + '...'
