# Generated by Django 4.1.4 on 2023-01-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidcredible', '0003_alter_review_body_alter_review_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
    ]
