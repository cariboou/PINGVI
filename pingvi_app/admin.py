from django.contrib import admin
from .models import Specialist, Approach, Therapy_session, Client

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'fist_name', 'approach', 'price', 'photo')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'approach',)
    list_filter = ('approach',)

class ApproachAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class Therapy_sessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialist', 'datetime', 'is_taken', 'client')
    list_display_links = ('id','datetime')
    search_fields = ('specialist', 'client')
    list_editable = ('is_taken',)
    list_filter = ('specialist','is_taken')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'fist_name', 'email', 'number_phone')
    list_display_links = ('id', 'last_name', 'email')
    search_fields = ('last_name', 'email')

admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Approach, ApproachAdmin)
admin.site.register(Therapy_session, Therapy_sessionAdmin)
admin.site.register(Client, ClientAdmin)

