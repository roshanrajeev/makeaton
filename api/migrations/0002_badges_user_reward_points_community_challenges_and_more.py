# Generated by Django 4.1.2 on 2022-10-26 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('image', models.TextField()),
                ('unlock_point', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='reward_points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('liked', models.PositiveIntegerField(default=0)),
                ('comment_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('commentedby', models.ManyToManyField(related_name='commentedby', to=settings.AUTH_USER_MODEL)),
                ('likedby', models.ManyToManyField(related_name='likedby', to=settings.AUTH_USER_MODEL)),
                ('postedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('days', models.IntegerField()),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('challengedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdby', to=settings.AUTH_USER_MODEL)),
                ('completedby', models.ManyToManyField(related_name='completedby', to=settings.AUTH_USER_MODEL)),
                ('joinedby', models.ManyToManyField(related_name='joinedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.challenges')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
