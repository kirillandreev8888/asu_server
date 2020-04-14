from django.db import models


# class User(models.Model):
#     login = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)

class Group(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=30)
    classroom = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    time = models.IntegerField()
    day = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.group.id)+":"+str(self.day) + "-" + str(self.time)

# class GroupLesson(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
# Create your models here.
