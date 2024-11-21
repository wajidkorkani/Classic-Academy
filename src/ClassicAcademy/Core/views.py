from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    
    Coaching_Classes = Coaching_Classes.objects.all()
    Coaching_Subjects = Coaching_Subjects.objects.all()
    English_Courses = English_Courses.objects.all()
    Courses = Courses.objects.all()
    Education_Programs = Education_Programs.objects.all()
    MS_Two_Year_Programs = MS_Two_Year_Programs.objects.all()
    BS_Four_Year_Programs = BS_Four_Year_Programs.objects.all()
    MBA = MBA.objects.all()
    Two_Year_Associate_Degree_Programs = Two_Year_Associate_Degree_Programs.objects.all()
    Diploma_Programs = Diploma_Programs.objects.all()
    Specialization_Certificate_Six_Months_Courses_Programs = models.objects.all()
    Facilties = Facilties.objects.all()

    template = "index.html"
    context = {
        'Coaching_Classes': Coaching_Classes,
        'Coaching_Subjects': Coaching_Subjects,
        'English_Courses': English_Courses,
        'Courses': Courses,
        'Education_Programs': Education_Programs,
        'MS_Two_Year_Programs': MS_Two_Year_Programs,
        'BS_Four_Year_Programs': BS_Four_Year_Programs,
        'MBA': MBA,
        'Two_Year_Associate_Degree_Programs': Two_Year_Associate_Degree_Programs,
        'Diploma_Programs': Diploma_Programs,
        'Specialization_Certificate_Six_Months_Courses_Programs': Specialization_Certificate_Six_Months_Courses_Programs,
        'Facilties': Facilties,
    }
    return render(request, template, context)