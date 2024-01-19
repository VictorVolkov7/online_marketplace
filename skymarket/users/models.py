from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class UserRoles(models.TextChoices):
    """
    Enumerate available user roles.
    """
    ADMIN = 'admin', _('admin')
    USER = 'user', _('user')


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    """
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name=_('email address'),
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('first name'),
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_('last name'),
    )
    phone = PhoneNumberField(
        verbose_name=_('phone'),
    )
    role = models.CharField(
        max_length=6,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name=_('role'),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_('May be needed for ban or account activation.'),
        verbose_name=_('active'),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('staff status'),
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('date joined'),
    )
    image = models.ImageField(
        upload_to='users/',
        null=True,
        blank=True,
        verbose_name=_('image')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role", "image"]

    objects = UserManager()

    @property
    def is_admin(self):
        """
        Check if user is admin
        """
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        """
        Check if user is user
        """
        return self.role == UserRoles.USER

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
