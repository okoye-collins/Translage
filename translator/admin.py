from django.contrib import admin
from .models import File, SentenceTokenize, TextToTranslate, Translation

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

# Register your models here.
admin.site.register(File)
admin.site.register(SentenceTokenize)
admin.site.register(TextToTranslate)
admin.site.register(Translation)