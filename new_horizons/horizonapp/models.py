from django.utils.text import slugify
from random import randint
from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
import datetime
from urllib.parse import urljoin 
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field

class NewsCategory(models.Model):

    name=models.CharField(max_length=255, verbose_name="Категорийн нэр", default='', unique=True)

    def __str__(self):
        return self.name

class News(models.Model):

    category=models.ForeignKey(NewsCategory, verbose_name="Мэдээний категори", on_delete=models.CASCADE)
    title=models.CharField(max_length=255, verbose_name="Мэдээний гарчиг", default='')
    pic=models.ImageField(verbose_name="Мэдээний зураг", upload_to="news/picture", default="", blank=True)
    content=CKEditor5Field('Text', config_name='extends')
    published_date=models.DateField(verbose_name="Огноо", auto_now=True, editable=False)
    slug=models.CharField(max_length=255, verbose_name="Мэдээний зам", default='', editable=False)
    featured=models.BooleanField(verbose_name="Онцлох мэдээ", default=False)
    viewed=models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        random_number = randint(1000, 999999999)
        while News.objects.filter(id=random_number).exists():
            random_number = randint(1000, 9999999)
        self.id = random_number

        self.slug = slugify("%s %s" % (self.category.name, str(self.id)))
        super().save(*args, **kwargs)

    
class BuildingRents(models.Model):

    floor1_a = models.BooleanField(default=False)
    def __str__(self):
        return "Түрээслэгч солих"
    class Meta:
        verbose_name = "Барилгын түрээсийн мэдээлэл"
        verbose_name_plural = "Барилгын түрээсийн мэдээлэл"


class ReasonBoxes(models.Model):

    box1_title=models.CharField(max_length=255, verbose_name="Box 1 гарчиг", null=False, default=None, blank=True)
    box1_text=models.TextField(verbose_name="Box 1 текст", null=False, default=None, blank=True)
    box2_title=models.CharField(max_length=255, verbose_name="Box 2 гарчиг", null=False, default=None, blank=True)
    box2_text=models.TextField(verbose_name="Box 2 текст", null=False, default=None, blank=True)
    box3_title=models.CharField(max_length=255, verbose_name="Box 3 гарчиг", null=False, default=None, blank=True)
    box3_text=models.TextField(verbose_name="Box 3 текст", null=False, default=None, blank=True)
    box4_title=models.CharField(max_length=255, verbose_name="Box 4 гарчиг", null=False, default=None, blank=True)
    box4_text=models.TextField(verbose_name="Box 4 текст", null=False, default=None, blank=True)
    box5_title=models.CharField(max_length=255, verbose_name="Box 5 гарчиг", null=False, default=None, blank=True)
    box5_text=models.TextField(verbose_name="Box 5 текст", null=False, default=None, blank=True)
    box6_title=models.CharField(max_length=255, verbose_name="Box 6 гарчиг", null=False, default=None, blank=True)
    box6_text=models.TextField(verbose_name="Box 6 текст", null=False, default=None, blank=True)
    box7_title=models.CharField(max_length=255, verbose_name="Box 7 гарчиг", null=False, default=None, blank=True)
    box7_text=models.TextField(verbose_name="Box 7 текст", null=False, default=None, blank=True)

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
    
    # subject=models.CharField(verbose_name="Сэдэв", max_length=255,  null=False, default=None)
    pdf=models.TextField(verbose_name="PDF link", null=False, default=None)

    class Meta:
        verbose_name = 'PDF брошур'
        verbose_name_plural = 'PDF брошур'


class FeatureCard(models.Model):
    box1_title=models.CharField(max_length=255, verbose_name="Box 1 гарчиг", null=True, blank=True, default=None)
    box1_text=models.TextField(verbose_name="Box 1 текст", null=True, blank=True, default=None)
    box2_title=models.CharField(max_length=255, verbose_name="Box 2 гарчиг", null=True, blank=True, default=None)
    box2_text=models.TextField(verbose_name="Box 2 текст", null=True, blank=True, default=None)
    box3_title=models.CharField(max_length=255, verbose_name="Box 3 гарчиг", null=True, blank=True, default=None)
    box3_text=models.TextField(verbose_name="Box 3 текст", null=True, blank=True, default=None)
    box4_title=models.CharField(max_length=255, verbose_name="Box 4 гарчиг", null=True, blank=True, default=None)
    box4_text=models.TextField(verbose_name="Box 4 текст", null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Санал болгох талбар'
        verbose_name_plural = 'Санал болгох талбар'
  
class OrganizationCategory(models.Model):
    category_name=models.CharField(max_length=255, verbose_name="Ангиллын нэр", null=True, blank=True, default=None, unique=True)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = 'Байгууллагын ангилал'
        verbose_name_plural = 'Байгууллагын ангилал'


class Organization(models.Model):
    or_name=models.CharField(max_length=255, verbose_name="Байгууллагын нэр", null=True, blank=True, default=None, unique=True)
    category=models.ForeignKey(OrganizationCategory, verbose_name="Байгуулагын категори", on_delete=models.CASCADE)
    pic=models.ImageField(upload_to="Organization/", verbose_name="Лого", default="", blank=True)
    special = models.BooleanField(verbose_name="Нүүр хуудсанд гаргах ", default=False)

    def __str__(self):
        return self.or_name

    class Meta:
        verbose_name = 'Байгууллагууд'
        verbose_name_plural = 'Байгууллагуудын жагсаалт'

class OrganizationDetail(models.Model):
    title=models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default=None)
    desc=models.TextField(verbose_name="Тайлбар", null=True, blank=True, default=None) 
    pic=models.ImageField(upload_to="Organization/Detail/", verbose_name="Зураг", default="", blank=True)
    organization=models.ForeignKey(Organization, verbose_name="Байгуулага", on_delete=models.CASCADE, default='')

class RentedFloor(models.Model):
    rented_object=models.CharField(max_length=255, verbose_name="Rented floor name", default='')
    organization=models.ForeignKey(Organization, verbose_name="Байгуулагын нэр", on_delete=models.CASCADE)

class ContactUs(models.Model):
    fullname=models.CharField(max_length=255, verbose_name="Нэр", default='')
    email=models.CharField(max_length=255, verbose_name="Цахим хаяг", default='')
    company=models.CharField(max_length=255, verbose_name="Компани нэр", default='')
    message=models.TextField(verbose_name="Тайлбар", default='') 

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Холбоо барих хүсэлт"
        verbose_name_plural = "Холбоо барих хүсэлт жагсаалт"



class BuildingIntro(models.Model):
        
    title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default=None)
    text = RichTextField()
    pic=models.ImageField(upload_to="Home/building_intro/", verbose_name="Зураг", default="", blank=True)

    class Meta:
        verbose_name = 'Барилгын товч танилцуулга'
        verbose_name_plural = 'Барилгын товч танилцуулга'


class FloorPlan(models.Model):
    floor = models.CharField(max_length=255, verbose_name="Давхар", null=True, blank=True, default="Оруулаагүй")
    title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="Оруулаагүй")
    description = CKEditor5Field('Text', config_name='extends')
    pic = models.ImageField(upload_to="Home/Plan-Pictures", verbose_name="План зураг", default='settings/index.jpeg', blank=True)


    class Meta:
        verbose_name = 'Давхрын план зураг, танилцуулга'
        verbose_name_plural = 'Давхрын план зураг, танилцуулга'


class HomeSlider(models.Model):
    CHOICES = (
        ('1', 'Брошур'),
        ('2', 'Холбоо барих'),
        ('3', 'Давхарын мэдээлэл')
    )

    button_choice = models.CharField(max_length=255, verbose_name="Товчны төрөл", default=CHOICES[0], choices=CHOICES)
    text_lil = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default=None)
    title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default=None)
    background_pic = models.ImageField(upload_to="Home", verbose_name="Зураг", default="", blank=True)

    choice1 = models.BooleanField(editable=False, default=False)
    choice2 = models.BooleanField(editable=False, default=False)
    choice3 = models.BooleanField(editable=False, default=False)

    def save(self, *args, **kwargs):
        print(self.button_choice)
        # TODO remove hard code
        if self.button_choice is self.CHOICES[0][0]:
            self.choice1 = True
            self.choice2 = False
            self.choice3 = False
        if self.button_choice is self.CHOICES[1][0]:
            self.choice1 = False
            self.choice2 = True
            self.choice3 = False
        if self.button_choice is self.CHOICES[2][0]:
            self.choice1 = False
            self.choice2 = False
            self.choice3 = True
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Нүүр хуудас - slider'