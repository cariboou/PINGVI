# Generated by Django 4.0 on 2021-12-23 08:40

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('number_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='BY')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, upload_to='photos/', verbose_name='Фото')),
                ('degree', models.TextField(max_length=100, verbose_name='Ученая степень')),
                ('awards_prizes', models.TextField(blank=True, max_length=200, verbose_name='Награды и премии')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('approach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pingvi_app.approach')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Therapy_session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время сеанса')),
                ('is_taken', models.BooleanField(verbose_name='Занято')),
                ('client', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pingvi_app.client', verbose_name='Клиент')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pingvi_app.specialist', verbose_name='Специалист')),
            ],
            options={
                'verbose_name': 'Сеанс психотерапии',
                'verbose_name_plural': 'Сеансы психотерапии',
                'ordering': ['datetime'],
            },
        ),
    ]
