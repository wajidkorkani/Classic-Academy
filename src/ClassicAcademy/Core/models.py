from django.db import models

# Create your models here.
class Coaching_Classes(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Coaching_Subjects(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class English_Courses(models.Model):
    topic = models.CharField(max_length=250)

    def __str__(self):
        return self.topic

class Courses(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Facilties(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Education_Programs(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class MS_Two_Year_Programs(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class BS_Four_Year_Programs(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class MBA(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Two_Year_Associate_Degree_Programs(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Diploma_Programs(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Specialization_Certificate_Six_Months_Courses_Programs(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Virtual_University_Courses_And_Programs(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class News_Feeds(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.CharField(max_length=3000)
    video = models.CharField(max_length=5000)

    def __str__(self):
        return self.name