# Generated by Django 3.2.9 on 2021-11-22 19:35

from django.db import migrations, models
import django.db.models.deletion
import store.utils.uploading


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('store', '0002_auto_20211121_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name=store.utils.uploading.upload_function),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='', verbose_name=store.utils.uploading.upload_function),
        ),
        migrations.CreateModel(
            name='ImageGalery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to=store.utils.uploading.upload_function)),
                ('use_in_slider', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Галерея изображений',
                'verbose_name_plural': 'Галерея изображений',
            },
        ),
    ]
