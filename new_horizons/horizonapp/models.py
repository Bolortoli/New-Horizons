from django.db import models

from ckeditor.fields import RichTextField

class NewsCategory(models.Model):

    name=models.CharField(max_length=255, verbose_name="Категорийн нэр", default='', unique=True)

    def __str__(self):
        return self.name

class News(models.Model):

    category=models.ForeignKey(NewsCategory, verbose_name="Мэдээний категори", on_delete=models.CASCADE)
    title=models.CharField(max_length=255, verbose_name="Мэдээний гарчиг", default='')
    # picture_main=models.ImageField(verbose_name="Гол зураг", upload_to='news/picture')
    # description1=models.TextField(verbose_name="Мэдээ 1", default='')
    content=RichTextField()
    floor1_a = models.BooleanField(default=False)
    floor1_b = models.BooleanField(default=False)
    floor2_a = models.BooleanField(default=False)
    
class BuildingRents(models.Model):

    floor1_a = models.BooleanField(default=False)
    floor1_b = models.BooleanField(default=False)
    floor2_a = models.BooleanField(default=False)
    floor2_b = models.BooleanField(default=False)
    floor3_a = models.BooleanField(default=False)
    floor3_b = models.BooleanField(default=False)
    floor4_a = models.BooleanField(default=False)
    floor4_b = models.BooleanField(default=False)
    floor5_a = models.BooleanField(default=False)
    floor5_b = models.BooleanField(default=False)
    floor6_a = models.BooleanField(default=False)
    floor6_b = models.BooleanField(default=False)
    floor7_a = models.BooleanField(default=False)
    floor7_b = models.BooleanField(default=False)
    floor8_a = models.BooleanField(default=False)
    floor8_b = models.BooleanField(default=False)
    floor9_a = models.BooleanField(default=False)
    floor9_b = models.BooleanField(default=False)
    floor10_a = models.BooleanField(default=False)
    floor10_b = models.BooleanField(default=False)
    floor11_a = models.BooleanField(default=False)
    floor11_b = models.BooleanField(default=False)
    floor12_a = models.BooleanField(default=False)
    floor12_b = models.BooleanField(default=False)
    floor13_a = models.BooleanField(default=False)
    floor13_b = models.BooleanField(default=False)
    floor14_a = models.BooleanField(default=False)
    floor14_b = models.BooleanField(default=False)
    floor15_a = models.BooleanField(default=False)
    floor15_b = models.BooleanField(default=False)