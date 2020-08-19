from django.db import models
from django.core.validators import FileExtensionValidator
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

class ReasonBoxes(models.Model):

    box1_title=models.CharField(max_length=255, verbose_name="Box 1 гарчиг", null=False, default=None)
    box1_text=models.TextField(verbose_name="Box 1 текст", null=False, default=None)
    box2_title=models.CharField(max_length=255, verbose_name="Box 2 гарчиг", null=False, default=None)
    box2_text=models.TextField(verbose_name="Box 2 текст", null=False, default=None)
    box3_title=models.CharField(max_length=255, verbose_name="Box 3 гарчиг", null=False, default=None)
    box3_text=models.TextField(verbose_name="Box 3 текст", null=False, default=None)
    box4_title=models.CharField(max_length=255, verbose_name="Box 4 гарчиг", null=False, default=None)
    box4_text=models.TextField(verbose_name="Box 4 текст", null=False, default=None)
    box5_title=models.CharField(max_length=255, verbose_name="Box 5 гарчиг", null=False, default=None)
    box5_text=models.TextField(verbose_name="Box 5 текст", null=False, default=None)
    box6_title=models.CharField(max_length=255, verbose_name="Box 6 гарчиг", null=False, default=None)
    box6_text=models.TextField(verbose_name="Box 6 текст", null=False, default=None)
    box7_title=models.CharField(max_length=255, verbose_name="Box 7 гарчиг", null=False, default=None)
    box7_text=models.TextField(verbose_name="Box 7 текст", null=False, default=None)

    class Meta:
        verbose_name = '7 шалтгаан'
        verbose_name_plural = '7 шалтгаан'

class Settings(models.Model):
    logo=models.ImageField(upload_to="settings", verbose_name="Барилгын лого", default="", blank=True)
    phone=models.CharField(max_length=255, verbose_name="Холбоо барих утас", null=False, default=None)
    mail=models.CharField(max_length=255, verbose_name="Компанийн э-мэйл хаяг", null=False, default=None)
    location=models.CharField(max_length=255, verbose_name="Барилгын байршил", null=False, default=None)
    facebook=models.CharField(max_length=255, verbose_name="Facebook хаяг", null=False, default=None)
    instagram=models.CharField(max_length=255, verbose_name="Instagram хаяг", null=False, default=None)
    twitter=models.CharField(max_length=255, verbose_name="Twitter хаяг", null=False, default=None)


    class Meta:
        verbose_name = 'Сайтын тохиргоо'
        verbose_name_plural = 'Сайтын тохиргоо'

class PDFbrochure(models.Model):
    
    subject=models.CharField(verbose_name="Сэдэв", max_length=255,  null=False, default=None)
    pdf=models.FileField(upload_to="brochure",verbose_name="Барилгын брошур",
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])], blank=False, default=None)
