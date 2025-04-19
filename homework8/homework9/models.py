from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    birthday = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=512)
    release_date = models.DateField()
    pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # тут, один автор може мати багато книжок, а одна книжка - одного автора
    language = models.CharField(max_length=128)


class Library(models.Models):
    adress = models.CharField(max_length=256)
    books = models.ManyToManyField(Book)


class Employee(models.Model):
    class Positions(models.TextChoices):
        admin = 1, 'administrator'
        average_employee = 2, 'average employee'
        security = 3, 'security'

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    birthday = models.DateField()
    position = models.CharField(choices=Positions.choices)
    sallary = models.IntegerField()

    library = models.ForeignKey(Library, on_delete=models.CASCADE) # тут, одна бібліотека може мати багато робочих, але один робочий - одну бібліотеку (роботу) 


class Customer(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    ''' 
    нижче, ідея в тому що покупець може бути прив'язаним до якихось кількох працівників бібліотеки.
    вони будуть типу радити якісь книжки
    ''' 
    my_employees = models.ManyToManyField(Employee)
