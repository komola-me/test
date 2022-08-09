# Generated by Django 4.0.6 on 2022-07-19 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(max_length=128, unique=True)),
                ('job_position', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(null=True)),
                ('location', models.CharField(max_length=128)),
                ('salary', models.PositiveBigIntegerField(default=0)),
                ('is_premium', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='author.author')),
                ('tag', models.ManyToManyField(related_name='vacancy', to='vacancy.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
