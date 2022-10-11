# Generated by Django 4.0.4 on 2022-10-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=250)),
                ('recipient', models.EmailField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
