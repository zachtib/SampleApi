from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    pub_date = models.DateField()

    def __str__(self):
        return self.title


