# third-party
from django_quill.fields import QuillField

#django
from django.db import models


class Tag(models.Model):
    """django data model tag"""

    name = models.CharField(
        'tag', 
        max_length=100
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Blog(models.Model):
    """Django data model Entrada"""

    title = models.CharField('titulo', max_length=200)
    author = models.CharField('autor', max_length=200)
    description = models.TextField('descripcion')
    content = QuillField()
    tag = models.ManyToManyField(
        Tag, 
        verbose_name='tag'
    )

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
