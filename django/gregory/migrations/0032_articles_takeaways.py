# Generated by Django 4.0.4 on 2022-11-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gregory', '0031_articles_crossref_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='takeaways',
            field=models.TextField(blank=True, null=True),
        ),
    ]
