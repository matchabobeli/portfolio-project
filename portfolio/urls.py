from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'certificates', views.CertificateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] 