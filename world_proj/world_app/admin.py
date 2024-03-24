from django.contrib import admin
from .models import City, Country, Countrylanguage
# Register your models here.
class cityAdmin(admin.ModelAdmin):
    list_display = ['id','name','countrycode','district','population']
    search_fields = ['name','countrycode','district']
    list_filter = ['countrycode','district']
    list_per_page = 10
class countryAdmin(admin.ModelAdmin):
    list_display = ['code','name','continent','region','surfacearea','indepyear','population','lifeexpectancy','gnp','gnpold','localname','governmentform','headofstate','capital','code2']
    search_fields = ['code','name','continent','region','surfacearea','indepyear','population','lifeexpectancy','gnp','gnpold','localname','governmentform','headofstate','capital','code2']
    list_filter = ['code','name','continent','region','surfacearea','indepyear','population','lifeexpectancy','gnp','gnpold','localname','governmentform','headofstate','capital','code2']
    list_per_page = 10
class countrylanguageAdmin(admin.ModelAdmin):
    list_display = ['countrycode','language','isofficial','percentage']
    search_fields = ['countrycode','language','isofficial','percentage']
    list_filter = ['countrycode','language','isofficial','percentage']
    list_per_page = 10
admin.site.register(City,cityAdmin)
admin.site.register(Country,countryAdmin)
admin.site.register(Countrylanguage,countrylanguageAdmin)