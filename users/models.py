from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractUser
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    USER_TYPE = (
        ('freelancer', 'Freelacer'),
        ('client', 'Client')
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars', default='media/R.png')
    languages = models.CharField(max_length=150, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class ConfirmationCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.email} - {self.code}'


class Portfolio(models.Model):
    name = models.CharField(max_length=70)
    proect_info = RichTextField()


class Freelancer(models.Model):
    STATUS_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermedia', 'Intermedia'),
        ('expert', 'Expert'),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    skills = models.ManyToManyField('Skill', related_name='freelancers')
    level = models.CharField(max_length=30, choices=STATUS_CHOICES)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    country = CountryField()
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
