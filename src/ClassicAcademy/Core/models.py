from django.db import models

# Create your models here.
class Coaching_Classes(models.Model):
    name = models.CharField(max_lenght=250)

class Coaching_Subjects(models.Model):
    name = models.CharField(max_lenght=250)

class English_Courses(models.Model):
    topic = models.CharField(max_lenght=250)

class Courses(models.Model):
    name = models.CharField(max_lenght=250)
    duration = models.CharField(max_lenght=250)

class Facilties(models.Model):
    name = models.CharField(max_lenght=250)

class Education_Programs(models.Model):
    name = models.CharField(max_lenght=250)

class MS_Two_Year_Programs(models.Model):
    name = models.CharField(max_lenght=250)
    duration = models.CharField(max_lenght=250)

class BS_Four_Year_Programs(models.Model):
    name = models.CharField(max_lenght=250)
    duration = models.CharField(max_lenght=250)

class MBA(models.Model):
    name = models.CharField(max_lenght=250)
    duration = models.CharField(max_lenght=250)

class Two_Year_Associate_Degree_Programs(models.Model):
    name = models.CharField(max_lenght=250)
    duration = models.CharField(max_lenght=250)

class Diploma_Programs(models.Model):
    name = models.CharField(max_lenght=250)
    duration = models.CharField(max_lenght=250)

class Specialization_Certificate_Six_Months_Courses_Programs(models.Model):
    name = models.CharField(max_lenght=250)
    duration = models.CharField(max_lenght=250)
