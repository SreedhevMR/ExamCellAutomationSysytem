# Generated by Django 5.1 on 2024-09-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_exam_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
