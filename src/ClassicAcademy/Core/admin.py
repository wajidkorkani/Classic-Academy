from django.contrib import admin
from .models import (
    Coaching_Classes, 
    Coaching_Subjects, 
    English_Courses, 
    Courses, 
    Facilties, 
    Education_Programs, 
    MS_Two_Year_Programs, 
    BS_Four_Year_Programs, 
    MBA, 
    Two_Year_Associate_Degree_Programs, 
    Diploma_Programs, 
    Specialization_Certificate_Six_Months_Courses_Programs
)

# Register each model with the admin panel
admin.site.register(Coaching_Classes)
admin.site.register(Coaching_Subjects)
admin.site.register(English_Courses)
admin.site.register(Courses)
admin.site.register(Facilties)
admin.site.register(Education_Programs)
admin.site.register(MS_Two_Year_Programs)
admin.site.register(BS_Four_Year_Programs)
admin.site.register(MBA)
admin.site.register(Two_Year_Associate_Degree_Programs)
admin.site.register(Diploma_Programs)
admin.site.register(Specialization_Certificate_Six_Months_Courses_Programs)
