# Generated by Django 3.0.6 on 2020-05-15 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200515_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-published_date', '-updated', '-timestamp']},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='pub_date',
            new_name='published_date',
        ),
    ]
