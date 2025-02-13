from django.db import models
from django.contrib.auth.models import User

class NonDeleted(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)

    everything = models.Manager()
    objects = NonDeleted()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True

class School(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Grade(models.Model):
    name = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.school} - {self.name}"
    
class Student(SoftDelete):
    name = models.CharField(max_length=20)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name