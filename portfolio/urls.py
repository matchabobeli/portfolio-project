from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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
    path('', views.home, name='home'),
    path('experience/', views.experience_page, name='experience'),
    path('education/', views.education_page, name='education'),
    path('skills/', views.skills_page, name='skills'),
    path('certificates/', views.certificates_page, name='certificates'),
    path('contact/', views.contact_page, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)