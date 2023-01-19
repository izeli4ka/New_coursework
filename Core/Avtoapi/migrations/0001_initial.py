# Generated by Django 4.1.5 on 2023-01-04 02:26

import Avtoapi.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=40, verbose_name='Почта')),
                ('date_of_reg', models.DateField(verbose_name='На портале с')),
                ('amount', models.FloatField(verbose_name='Оценка пользователя')),
                ('saler', models.BooleanField(null=True, verbose_name='Является продавцом')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название поста продажи')),
                ('discription', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(null=True, validators=[Avtoapi.models.validate_price], verbose_name='Цена')),
                ('photo', models.FileField(upload_to='photos', verbose_name='Фото авто')),
                ('saler', models.ManyToManyField(to='Avtoapi.user', verbose_name='Имя продавца')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название новости')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('likes', models.IntegerField(validators=[Avtoapi.models.validate_likes], verbose_name='Количество лайков')),
                ('photo', models.FileField(upload_to='photos', verbose_name='Фото новости')),
                ('author', models.ManyToManyField(to='Avtoapi.user', verbose_name='Автор новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Нововсти',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=40, verbose_name='Почта')),
                ('date_of_reg', models.DateField(verbose_name='На портале с')),
                ('amount', models.FloatField(verbose_name='Оценка пользователя')),
                ('saler', models.BooleanField(null=True, verbose_name='Является продавцом')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Пользователь',
                'verbose_name_plural': 'historical Пользователи',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSale',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название поста продажи')),
                ('discription', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(null=True, validators=[Avtoapi.models.validate_price], verbose_name='Цена')),
                ('photo', models.TextField(max_length=100, verbose_name='Фото авто')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Пост',
                'verbose_name_plural': 'historical Посты',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalNews',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название новости')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('likes', models.IntegerField(validators=[Avtoapi.models.validate_likes], verbose_name='Количество лайков')),
                ('photo', models.TextField(max_length=100, verbose_name='Фото новости')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Новость',
                'verbose_name_plural': 'historical Нововсти',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
