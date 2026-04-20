from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile, Experience, Education, Skill, Certificate
from .serializers import ProfileSerializer, ExperienceSerializer, EducationSerializer, SkillSerializer, CertificateSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

def home(request):
    return render(request, 'home.html')

def experience_page(request):
    return render(request, 'experience.html')

def education_page(request):
    return render(request, 'education.html')

def skills_page(request):
    return render(request, 'skills.html')

def certificates_page(request):
    return render(request, 'certificates.html')

def contact_page(request):
    return render(request, 'contact.html')