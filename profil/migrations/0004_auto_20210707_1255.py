# Generated by Django 3.2.5 on 2021-07-07 12:55

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0003_auto_20210707_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepage',
            name='address',
        ),
        migrations.AlterField(
            model_name='profilepage',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Vorname'),
        ),
        migrations.AlterField(
            model_name='profilepage',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Familienname'),
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kurstitel')),
                ('provider', models.CharField(max_length=100, verbose_name='Anbieter')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('profile', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='profil.profilepage')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titel')),
                ('provider', models.TextField(max_length=100, verbose_name='Arbeitgeber')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('profile', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='employments', to='profil.profilepage')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titel')),
                ('provider', models.TextField(max_length=100, verbose_name='Schule/Hochschule')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('from_date', models.DateField(verbose_name='Von')),
                ('to_date', models.DateField(verbose_name='Bis')),
                ('profile', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='profil.profilepage')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultantRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titel')),
                ('profile', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultant_roles', to='profil.profilepage')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titel')),
                ('provider', models.CharField(max_length=100, verbose_name='Aussteller')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('profile', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='profil.profilepage')),
            ],
        ),
    ]