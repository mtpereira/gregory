# Generated by Django 4.0.4 on 2022-11-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gregory', '0030_alter_articles_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='crossref_check',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]