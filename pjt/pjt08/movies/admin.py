from django.contrib import admin
from .models import Review, Movie, Actor

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Actor)