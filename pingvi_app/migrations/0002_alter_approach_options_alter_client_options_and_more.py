# Generated by Django 4.0 on 2021-12-23 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pingvi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='approach',
            options={'ordering': ['name'], 'verbose_name': 'Approach'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['last_name'], 'verbose_name': 'Client'},
        ),
        migrations.AlterModelOptions(
            name='specialist',
            options={'ordering': ['last_name'], 'verbose_name': 'Specialist'},
        ),
        migrations.AlterModelOptions(
            name='therapy_session',
            options={'ordering': ['datetime'], 'verbose_name': 'Therapy session'},
        ),
        migrations.AlterField(
            model_name='approach',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Approach'),
        ),
        migrations.AlterField(
            model_name='client',
            name='fist_name',
            field=models.CharField(max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='approach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pingvi_app.approach', verbose_name='Approach'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='awards_prizes',
            field=models.TextField(blank=True, max_length=200, verbose_name='Avards and prizes'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='degree',
            field=models.TextField(max_length=100, verbose_name='Degree'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='fist_name',
            field=models.CharField(max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='therapy_session',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pingvi_app.client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='therapy_session',
            name='datetime',
            field=models.DateTimeField(verbose_name='Datetime'),
        ),
        migrations.AlterField(
            model_name='therapy_session',
            name='is_taken',
            field=models.BooleanField(verbose_name='Is taken'),
        ),
        migrations.AlterField(
            model_name='therapy_session',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pingvi_app.specialist', verbose_name='Specialist'),
        ),
    ]
