# Generated by Django 3.2 on 2023-05-11 12:55

from django.db import migrations

def transfer_tage(apps, schema_editor):
    Article = apps.get_model('website.Article')
    for article in Article.objects.all():
        article.tags.set(article.tags_old.all())

def rollback(apps, schema_editor):
    Article = apps.get_model('website.Article')
    for article in Article.objects.all():
        article.tags_old.set(article.tags.all())


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20230511_1854'),
    ]

    operations = [
        migrations.RunPython(transfer_tage, transfer_tage, rollback)
    ]