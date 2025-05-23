# Generated by Django 5.0.6 on 2024-06-24 16:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_logo_ecole_delete_enspd'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_matieres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='image_matiere/')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='logo_ecole',
            name='image',
            field=models.ImageField(upload_to='image_logo_ecole/'),
        ),
        migrations.AlterField(
            model_name='logo_ecole',
            name='titre_ecole',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('pdf', models.FileField(upload_to='pdfs_epreuve/')),
                ('date_consultation', models.DateTimeField(auto_now_add=True)),
                ('upload_at', models.DateTimeField(auto_now=True)),
                ('ecole', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.logo_ecole')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.image_matieres')),
                ('niveau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.niveau')),
            ],
        ),
        migrations.CreateModel(
            name='Correction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='pdfs_epreuve/')),
                ('date_consultation', models.DateTimeField(auto_now_add=True)),
                ('upload_at', models.DateTimeField(auto_now=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('epreuve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.epreuve')),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_consultation', models.DateTimeField(auto_now_add=True)),
                ('upload_at', models.DateTimeField(auto_now=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.image_matieres')),
                ('niveau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.niveau')),
            ],
        ),
    ]
