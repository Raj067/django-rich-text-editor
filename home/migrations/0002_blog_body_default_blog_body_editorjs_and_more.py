# Generated by Django 4.1.2 on 2022-12-07 09:53

from django.db import migrations, models
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body_default',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='body_editorjs',
            field=django_editorjs_fields.fields.EditorJsJSONField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='body_editorjs_text',
            field=django_editorjs_fields.fields.EditorJsTextField(default='!'),
            preserve_default=False,
        ),
    ]
