# Generated by Django 4.2.2 on 2023-09-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_lessonview_is_viewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='products',
        ),
        migrations.AddField(
            model_name='productaccess',
            name='lessons',
            field=models.ManyToManyField(related_name='products', to='api.lesson'),
        ),
    ]
