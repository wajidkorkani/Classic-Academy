from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    # Rename variables to avoid conflicts with model names
    coaching_classes = Coaching_Classes.objects.all()
    coaching_subjects = Coaching_Subjects.objects.all()
    english_courses = English_Courses.objects.all()
    courses = Courses.objects.all()
    education_programs = Education_Programs.objects.all()
    ms_two_year_programs = MS_Two_Year_Programs.objects.all()
    bs_four_year_programs = BS_Four_Year_Programs.objects.all()
    mba = MBA.objects.all()
    two_year_associate_degree_programs = Two_Year_Associate_Degree_Programs.objects.all()
    diploma_programs = Diploma_Programs.objects.all()
    specialization_certificate_six_months_courses_programs = Specialization_Certificate_Six_Months_Courses_Programs.objects.all()
    facilities = Facilties.objects.all()

    # Pass the updated variable names to the context
    context = {
        'coaching_classes': coaching_classes,
        'coaching_subjects': coaching_subjects,
        'english_courses': english_courses,
        'courses': courses,
        'education_programs': education_programs,
        'ms_two_year_programs': ms_two_year_programs,
        'bs_four_year_programs': bs_four_year_programs,
        'mba': mba,
        'two_year_associate_degree_programs': two_year_associate_degree_programs,
        'diploma_programs': diploma_programs,
        'specialization_certificate_six_months_courses_programs': specialization_certificate_six_months_courses_programs,
        'facilities': facilities,
    }

    # Specify your template and return the rendered response
    template = "index.html"
    return render(request, template, context)
