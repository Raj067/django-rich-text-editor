from django.db import models
from django_editorjs_fields import EditorJsJSONField  # Django >= 3.1
from django_editorjs_fields import EditorJsTextField
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    body_default = models.TextField()
    body_editorjs = EditorJsJSONField()  # Django >= 3.1
    body_editorjs_text = EditorJsTextField()
