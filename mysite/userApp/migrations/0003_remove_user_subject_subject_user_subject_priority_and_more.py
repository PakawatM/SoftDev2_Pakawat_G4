# Generated by Django 4.1.7 on 2023-03-16 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpApp', '0005_alter_subject_final_alter_subject_mid_term'),
        ('userApp', '0002_user_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_subject',
            name='subject',
        ),
        migrations.AddField(
            model_name='user_subject',
            name='priority',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AddField(
            model_name='user_subject',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpApp.section'),
        ),
    ]