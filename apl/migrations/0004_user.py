# Generated by Django 3.2.12 on 2024-02-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0003_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.IntegerField()),
                ('categories', models.CharField(choices=[('Category1', 'Category1'), ('Category2', 'Category2'), ('Category3', 'Category3')], max_length=50)),
            ],
        ),
    ]