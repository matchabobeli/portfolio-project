from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile, Experience, Education, Skill, Certificate
from .serializers import ProfileSerializer, ExperienceSerializer, EducationSerializer, SkillSerializer, CertificateSerializer

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

    from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def cv(request):
    return render(request, 'cv.html')

def certificates_page(request):
    return render(request, 'certificates.html')