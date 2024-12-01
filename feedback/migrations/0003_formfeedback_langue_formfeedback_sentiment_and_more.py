# Generated by Django 5.0.6 on 2024-12-01 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_rename_platform_socialmediafeedback_langue'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfeedback',
            name='langue',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='formfeedback',
            name='sentiment',
            field=models.CharField(choices=[('positive', 'Positive'), ('neutral', 'Neutral'), ('negative', 'Negative')], default='Neutral', max_length=20),
        ),
        migrations.AddField(
            model_name='qrcodefeedback',
            name='langue',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='qrcodefeedback',
            name='sentiment',
            field=models.CharField(choices=[('positive', 'Positive'), ('neutral', 'Neutral'), ('negative', 'Negative')], default='Neutral', max_length=20),
        ),
        migrations.AlterField(
            model_name='socialmediafeedback',
            name='langue',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='socialmediafeedback',
            name='sentiment',
            field=models.CharField(choices=[('positive', 'Positive'), ('neutral', 'Neutral'), ('negative', 'Negative')], default='Neutral', max_length=20),
        ),
    ]
