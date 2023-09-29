# Generated by Django 4.2.2 on 2023-09-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_product_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonview',
            old_name='duration_view',
            new_name='viewed_seconds',
        ),
        migrations.RemoveField(
            model_name='lessonview',
            name='is_viewed',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='info',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Access',
        ),
    ]
