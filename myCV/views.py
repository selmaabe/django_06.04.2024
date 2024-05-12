from django.shortcuts import render
from myCV.models import GeneralSetting, ImageSetting,Skill,Experience,Education


# Create your views here.

def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_title = GeneralSetting.objects.get(name="home_banner_title").parameter
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameter
    home_banner_description = GeneralSetting.objects.get(name="home_banner_description").parameter
    testimonial_1 = GeneralSetting.objects.get(name='testimonial_1').parameter
    testimonial_2 = GeneralSetting.objects.get(name='testimonial_2').parameter
    clients = GeneralSetting.objects.get(name='clients').parameter
    client_satisfaction = GeneralSetting.objects.get(name='client_satisfaction').parameter
    project_ongoing = GeneralSetting.objects.get(name='project_ongoing').parameter
    project_compleate = GeneralSetting.objects.get(name='project_compleate').parameter

    # Images
    site_favicon = ImageSetting.objects.get(name='site_favicon').file
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    testimonial_1_image = ImageSetting.objects.get(name='testimonial_1_image').file
    testimonial_2_image = ImageSetting.objects.get(name='testimonial_2_image').file

    #Skills
    skills = Skill.objects.all()

    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-start_date')

    context = {'site_title': site_title,
               'site_keywords': site_keywords,
               'site_description': site_description,
               "home_banner_title": home_banner_title,
               "home_banner_name": home_banner_name,
               "home_banner_description": home_banner_description,
               "site_favicon": site_favicon,
               "home_banner_image": home_banner_image,
               "testimonial_1_image": testimonial_1_image,
               "testimonial_2_image": testimonial_2_image,
               "testimonial_1": testimonial_1,
               "testimonial_2": testimonial_2,
               "project_ongoing": project_ongoing,
               "client_satisfaction": client_satisfaction,
               "clients": clients,
               "project_compleate": project_compleate,
               "skills":skills,
               "experiences":experiences,
               "educations":educations,

               }

    return render(request, 'index.html', context=context)
