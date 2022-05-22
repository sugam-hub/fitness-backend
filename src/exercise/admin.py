from django.contrib import admin

from exercise.models import Exercise
from .models import *
# Register your models here.
admin.site.register(Exercise)
