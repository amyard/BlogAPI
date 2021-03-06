from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.text import slugify

from model_utils.models import TimeStampedModel


def gen_slug(s):
    new_slug = slugify(s, allow_unicode = True)
    return new_slug


def save_image_path(instance, filename):
    filename = instance.slug + '.jpg'
    date = instance.created.strftime("%Y-%m-%d %H:%M:%S").split(' ')[0]
    return f'posts_pics/{date}/{instance.slug}/{filename}'


class Post(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(_('Title'), max_length=255, unique=True)
    slug = models.SlugField(_('Slug'), max_length=255, unique=True, blank=True)
    content = models.TextField(_('Content'))
    image = models.ImageField(default='default.png', upload_to=save_image_path, blank=True)

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
