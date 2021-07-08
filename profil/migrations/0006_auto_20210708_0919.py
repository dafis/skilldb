# Generated by Django 3.2.5 on 2021-07-08 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('profil', '0005_auto_20210707_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameField(
            model_name='employment',
            old_name='provider',
            new_name='employer',
        ),
        migrations.DeleteModel(
            name='ConsultantRolePage',
        ),
    ]
