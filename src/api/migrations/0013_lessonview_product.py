# Generated by Django 4.2.2 on 2023-09-30 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_productaccess_lessons_product_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonview',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.product'),
            preserve_default=False,
        ),
    ]
