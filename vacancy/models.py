from django.db import models
from users.models import Client


# Create your models here.

class Vacancy(models.Model):
    LEVELS = {
        ('begginer', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert')
    }

    title = models.CharField(max_length=100)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField()
    pay = models.DecimalField(max_digits=17, decimal_places=2)
    tags = models.ManyToManyField('Tag')
    required_level = models.CharField(max_length=20, choices=LEVELS)
    project_length = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveBigIntegerField(default=0)
    applications = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'{self.owner} - {self.title}'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
