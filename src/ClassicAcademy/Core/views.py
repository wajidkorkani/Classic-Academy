from django.shortcuts import render
from .models import *

# This function will delete all videos models and it will leave only one which is the new video link or recently uploaded video link
def Classic_Video_limit_manager():
    videos = Classic_Video.objects.all()
    if videos.count() > 1:
        videos_to_delete = videos.order_by('-id')[1:]
        for video in videos_to_delete:
            video.delete()

# Home page or landing page
def home(request):
    # Rename variables to avoid conflicts with model names
    virtual_university_courses_and_programs = Virtual_University_Courses_And_Programs.objects.all()
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
    video = Classic_Video.objects.all()
    Classic_Video_limit_manager()

    # Pass the updated variable names to the context
    context = {
        'Classic_Video': Classic_Video,
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
        'virtual_university_courses_and_programs': virtual_university_courses_and_programs,
        'videos': video
    }

    # Specify your template and return the rendered response
    template = "index.html"
    return render(request, template, context)



def Classic_NewsFeed_limit_manager():
    newsFeeds = News_Feeds.objects.all()
    if newsFeeds.count() > 3:
        news_to_delete = newsFeeds.order_by('-id')[3:]
        for news in news_to_delete:
            news.delete()

# This is newsFeed section 
def newsFeed(request):
    newsFeeds = News_Feeds.objects.all()
    Classic_NewsFeed_limit_manager()
    template = "newsFeed.html"
    context = {
        'newsFeeds': newsFeeds
    }
    return render(request, template, context)