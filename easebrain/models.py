from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone
from uuid import uuid4


class UserManager(BaseUserManager):
    """ users manager model """
    def _create_user(self, email, password, is_staff, is_superuser, **extrafields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
                email=email,
                password=password,
                is_staff=is_staff,
                is_active=True,
                is_superuser=is_superuser,
                created_at=now,
                updated_at=now,
                **extrafields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extrafields):
        """ user creation function """
        return self._create_user(email, password, False, False, **extrafields)

    def create_superuser(self, email, password, **extrafields):
        """ superuser creation functon """
        return self._create_user(email, password, True, True, **extrafields)


class User(AbstractBaseUser, PermissionsMixin):
    """ custom user class model """
    user_id = models.CharField(null=True, blank=True, max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(null=True, blank=True, max_length=200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        """ absolute url """
        return "/users/%i/" % (self.pk)

    def save(self, *args, **kwargs):
        """saving"""
        if self.user_id is None:
            self.user_id = str(uuid4()).split('-')[4]
        self.updated_at = timezone.localtime(timezone.now())

        super(User, self).save(*args, **kwargs)
