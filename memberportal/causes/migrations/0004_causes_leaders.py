# Generated by Django 2.1.5 on 2019-01-28 04:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('causes', '0003_causefund'),
    ]

    operations = [
        migrations.AddField(
            model_name='causes',
            name='leaders',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
