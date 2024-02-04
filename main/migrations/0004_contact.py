# Generated by Django 3.2.23 on 2024-02-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
