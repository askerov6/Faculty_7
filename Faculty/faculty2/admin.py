from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Faculty)
class MovieAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Prov)
admin.site.register(Stu)
admin.site.register(Well)
admin.site.register(Cabinet)
admin.site.register(Schedule)


