from modeltranslation.translator import TranslationOptions,translator
from .models import NewsCategory

class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)

translator.register(NewsCategory, NewsCategoryTranslationOptions)
