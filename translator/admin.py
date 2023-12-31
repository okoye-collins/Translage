from django.contrib import admin
from .models import SentenceTokenize,  File, Translation

# class TranslationInline(admin.StackedInline):
#     model = Translation
#     extra = 1
#     fields = ['language','translation']

# @admin.register(TextToTranslate)
# class TextToTranslateAdmin(admin.ModelAdmin):
#     model = TextToTranslate
#     list_display = ['text','language']
#     inlines = [TranslationInline]

# @admin.register(Translation)
# class TranslationAdmin(admin.ModelAdmin):
#     model = Translation
#     list_display = ['totranslate','language','translation']

class Translationinline(admin.TabularInline):
    model = Translation

class SentenceTokenizeAdmin(admin.ModelAdmin):
    inlines = [Translationinline]
    class Meta:
        model = SentenceTokenize

# Register your models here.
admin.site.register(File)
admin.site.register(SentenceTokenize, SentenceTokenizeAdmin)
admin.site.register(Translation)