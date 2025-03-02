from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is required")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)

ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')], default='Member')

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} - {self.role}"

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(default=timezone.now)
    isbn = models.CharField(max_length=13, default='default-isbn')

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can edit book details"),
            ("can_delete_book", "Can delete a book"),
            ("can_view_book", "Can view book details"),  # 🔄 Added a view permission for completeness
        ]

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
