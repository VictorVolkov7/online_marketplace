from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    """
    Model for Ad.
    """
    title = models.CharField(
        max_length=200,
        verbose_name=_('title'),
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name=_('price'),
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('author'),

    )
    image = models.ImageField(
        upload_to='Ad/',
        null=True,
        blank=True,
        verbose_name=_('image')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.price}: {self.author}'

    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')
        ordering = ['created_at']


class Comment(models.Model):
    """
    Model for Comment.
    """
    text = models.TextField(
        max_length=1500,
        verbose_name=_('text'),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('author'),
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('ad'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.created_at}'

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['created_at']
