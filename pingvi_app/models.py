from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Specialist(models.Model):
    fist_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='photos/', blank=True, verbose_name='Фото')
    approach = models.ForeignKey('Approach', on_delete=models.CASCADE, verbose_name='Направление в психотерапии')
    degree = models.TextField(max_length=100, verbose_name='Научная степень')
    awards_prizes = models.TextField(max_length=200, blank=True, verbose_name='Награды и достижения')
    price = models.IntegerField(verbose_name='Стоимость сеанса')

    def __str__(self):
        return f'{self.fist_name} {self.last_name}'

    class Meta:
        verbose_name = 'Специалист'
        ordering = ['last_name']
    

class Approach(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название направления')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Направление в психотерапии'
        ordering = ['name']


class Therapy_session(models.Model):
    specialist = models.ForeignKey('Specialist', on_delete=models.CASCADE, verbose_name='Специалист')
    datetime = models.DateTimeField(verbose_name='Дата и время сеанса')
    is_taken = models.BooleanField(verbose_name='Занят')
    client = models.ForeignKey('Client', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Клиент')

    def __str__(self):
        return str(self.datetime)[:19]

    class Meta:
        verbose_name = 'Сеанс психотерапии'
        ordering = ['datetime']

class Client(models.Model):
    fist_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='E-mail')
    number_phone = PhoneNumberField(region = 'BY')

    def __str__(self):
        return f'{self.fist_name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        ordering = ['last_name']







