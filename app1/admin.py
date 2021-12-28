from django.contrib import admin
from . models import problem
from . models import solutions
from . models import test

admin.site.register(problem),
admin.site.register(solutions),
admin.site.register(test)
