from django.contrib import admin
from .models import Profile, Experience, Education, Skill, Certificate

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Certificate)