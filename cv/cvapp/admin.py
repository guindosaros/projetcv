from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

class SpecialiteInline(admin.TabularInline):
      model = models.Specialite
      extra = 0
      
class DetailCompetenceInline(admin.TabularInline):
      model = models.DetailCompetence
      extra = 0


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'view_image',
        'user',
        'specialite',
        'email',
        'numero',
        'status',
        'date_add',
    )
    list_filter = (
        'user',
        'status',
        'date_add',
        'date_upd',
    )
    search_field = ('email')
    readonly_fields = ['detail_image']
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer un Profile')
    active.short_description = 'active un Profile'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver un Profile')
    desactive.short_description = 'desactive Profile'
    ordering = ('email',)
    list_per_page = 5
    date_hierarchy = ('date_add')
    
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.photo.url))

    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.photo.url))


class DetailsAdmin(admin.ModelAdmin):

    list_display = (
        'view_image',
        'presentation',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_field = ('presentation')
    readonly_fields = ['detail_image']
    def active(self, request, queryset):
        queryset.update(status = True)
        self.message_user(request, 'Activer un Detail')
    active.short_description = 'active un Detail'

    def desactive(self, request, queryset):
        queryset.update(status = False)
        self.message_user(request, 'Desactiver un Detail')
    desactive.short_description = 'desactive Detail'
    ordering = ('presentation',)
    list_per_page = 5
    date_hierarchy = ('date_add')
    
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

class AboutAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    inlines = [SpecialiteInline]


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = (
        'about',
        'nom',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'about',
        'status',
        'date_add',
        'date_upd',
    )


class EducationAdmin(admin.ModelAdmin):

    list_display = (
        'diplome',
        'slug',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('slug',)


class CompetenceAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )
    inlines = [DetailCompetenceInline]

class DetailCompetenceAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'competence',
        'pourcentage',
        'classe',
        'animate',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'competence',
        'status',
        'date_add',
        'date_upd',
    )


class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'annee',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


class MessageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'email',
        'sujet',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
_register(models.Details, DetailsAdmin)
_register(models.About, AboutAdmin)
_register(models.Specialite, SpecialiteAdmin)
_register(models.Education, EducationAdmin)
_register(models.Competence, CompetenceAdmin)
_register(models.DetailCompetence, DetailCompetenceAdmin)
_register(models.Experience, ExperienceAdmin)
_register(models.Service, ServiceAdmin)
_register(models.Message, MessageAdmin)
