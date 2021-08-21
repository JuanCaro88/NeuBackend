from django.contrib import admin
from .models import Countrie

# Register your models here.
class CountriesAdmin(admin.ModelAdmin):
    '''
    This class will represent of the visual in django admin
    '''

    list_display = (
        'name_countrie',
        'city',
        'state',
        'population'
    )

    search_fields = (
        'name_countrie',
        'city',
        'state',
    )

    list_filter = (
        'name_countrie',
        'city',
        'state',
    )




admin.site.register(Countrie, CountriesAdmin)
