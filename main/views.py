from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    return render(request, "index.html")


# def portfolio(request):
#     return render(request,"portfolio.html")



def blog(request):
    return render(request,"blog.html")


def portfolio(request):
    data = bio.objects.all()
    education = Education.objects.all()
    personalinfo = PersonalInfo.objects.all()
    extendedbio = ExtendedBio.objects.all()
    workexp = WorkExperience.objects.all()
    certification = Certification.objects.all()
    award = Award.objects.all()
    project = Project.objects.all()
    skill = Skill.objects.all()
    contactmessage = ContactMessage.objects.all()
    socialmedia = SocialMediaLink.objects.all()


    context = {'data': data, 'education':education,' personalinfo': personalinfo,'extendedbio':extendedbio,'workexp':workexp, 'certification':certification,'award': award,'project':project,'skill':skill, 'contactmessage': contactmessage,'socialmedia':socialmedia}
    return render(request, 'portfolio.html',context)
      
# def education(request):
#     data = Education.objects.all()
#     print(data)
#     context = {'education':data}
#     return render(request, 'portfolio.html',context)
