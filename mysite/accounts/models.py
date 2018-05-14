from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy
import uuid as uuid_lib
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)
    username_validator = UnicodeUsernameValidator()
    
    username = models.CharField(
        gettext_lazy('username'),
        max_length=150,
        unique=True,
        help_text=gettext_lazy(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_only.'),
        validators=[username_validator],
        error_messages={
            'unique':gettext_lazy("A user with that username already exists."),
        },
    )
    full_name = models.CharField(gettext_lazy('name'), max_length=150, blank=True)
    is_staff = models.BooleanField(
        gettext_lazy('staff status'),
        default=False,
        help_text=gettext_lazy(
            'Designates whether the user can log into this admin site.'),
    )    
    is_active = models.BooleanField(
        gettext_lazy('active'),
        default=True,
        help_text=gettext_lazy(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']
    
    class Meta:
        verbose_name = gettext_lazy('user')
        verbose_name_plural = gettext_lazy('users')
        abstract = True

    def get_full_name(self):
        return self.full_name.strip()