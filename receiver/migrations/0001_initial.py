# Generated by Django 3.1 on 2020-09-16 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
                ('message', models.CharField(blank=True, default='', max_length=100)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
