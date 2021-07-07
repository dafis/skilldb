# Generated by Django 3.2.5 on 2021-07-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='ProfilePage',
        ),
    ]
