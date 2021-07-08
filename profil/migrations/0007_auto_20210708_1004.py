# Generated by Django 3.2.5 on 2021-07-08 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('profil', '0006_auto_20210708_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='softskill',
            name='description',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='provider',
            field=models.CharField(max_length=100, verbose_name='Instution'),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='education',
            name='from_date',
            field=models.DateField(verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='education',
            name='provider',
            field=models.TextField(max_length=100, verbose_name='Institution'),
        ),
        migrations.AlterField(
            model_name='education',
            name='to_date',
            field=models.DateField(verbose_name='To'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='employer',
            field=models.TextField(max_length=100, verbose_name='Employer'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='profilepage',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='profilepage',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profilepage',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profilepage',
            name='profile_image',
            field=models.ForeignKey(help_text='Profile Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='softskill',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='training',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='training',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='training',
            name='provider',
            field=models.CharField(max_length=100, verbose_name='Provider'),
        ),
    ]
