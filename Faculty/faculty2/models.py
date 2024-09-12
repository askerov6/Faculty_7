from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=99)
    description = models.TextField()

    def __str__(self):
        return self.name


class Prov(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=99)
    bio = models.TextField()


class Stu(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField()


class Well(models.Model):
    name = models.CharField(max_length=99)
    code = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Prov, on_delete=models.CASCADE)


class Cabinet(models.Model):
    room_number = models.CharField(max_length=100)
    building = models.CharField(max_length=99)
    capacity = models.PositiveIntegerField()


class Schedule(models.Model):
    course = models.ForeignKey(Well, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10)



