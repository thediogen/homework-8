import datetime

from django.db import models
from django.utils.timezone import now

# Create your models here.


class Group(models.Model):
    number = models.SmallIntegerField()
    motto = models.CharField(max_length=128)
    meeting_room = models.SmallIntegerField() # тут напевно краще номер кабінету ніж назва


# замість "модель літератури бібліотеки" я зроблю модель бібліотеки і модель книжки бо так зручніше
# тоді, в бібліотеки будуть різні книжки


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    release_date = models.DateField()


class Library(models.Model):
    books = models.ManyToManyField(Book)
    employee = models.CharField(max_length=128)


class LibCard(models.Model):
    expiration_time = 30 # це час, за який картка буде не дійсна. указую в днях

    issued_at = now()
    expires_at = issued_at + datetime.timedelta(days=expiration_time)

    date_of_issue = models.DateField(default=issued_at)
    end_date = models.DateField(default=expires_at)

    price = models.DecimalField(max_digits=6, decimal_places=2)


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    student_card_num = models.PositiveIntegerField()
    addres = models.TextField()

    group = models.ForeignKey(Group, on_delete=models.PROTECT )
    lib_card = models.ForeignKey(LibCard, on_delete=models.CASCADE)


class OweBook(models.Model):
    lib_card = models.ForeignKey(LibCard, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    owe_date = models.DateField(default=now())
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
