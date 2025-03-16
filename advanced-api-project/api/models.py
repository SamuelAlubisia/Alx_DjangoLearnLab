from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150) # String field for the author's name

    def __str__(self):
        return self.name # Returns the author's name when printed

class Book(models.Model):
    title = models.CharField(max_length=200) #String field for the author's name
    publication_year = models.IntegerField()  # Integer field for the year published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') #One to many relationship between the Author model and the Book model

    def __str__(self):
        return f"{self.title} ({self.publication_year})"  # Returns title with year when printed