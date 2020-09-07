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
    class Meta:
        verbose_name = "Мэдээний категори"
        verbose_name_plural = "Мэдээний категори"

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

    class Meta:
        verbose_name = "Мэдээ"
        verbose_name_plural = "Мэдээ"

class BuildingRents(models.Model):

    floor1_a = models.BooleanField(default=False)
    def __str__(self):
        return "Түрээслэгч солих"
    class Meta:
        verbose_name = "Барилгын түрээсийн мэдээлэл"
        verbose_name_plural = "Барилгын түрээсийн мэдээлэл"


class ReasonBoxes(models.Model):

    box1_title=models.CharField(max_length=255, verbose_name="Box 1 гарчиг", default='Оруулаагүй', blank=True)
    box1_text=models.TextField(verbose_name="Box 1 текст", default='Оруулаагүй', blank=True)
    box2_title=models.CharField(max_length=255, verbose_name="Box 2 гарчиг", null=False, default='Оруулаагүй', blank=True)
    box2_text=models.TextField(verbose_name="Box 2 текст", default='Оруулаагүй', blank=True)
    box3_title=models.CharField(max_length=255, verbose_name="Box 3 гарчиг", default='Оруулаагүй', blank=True)
    box3_text=models.TextField(verbose_name="Box 3 текст", default='Оруулаагүй', blank=True)
    box4_title=models.CharField(max_length=255, verbose_name="Box 4 гарчиг", default='Оруулаагүй', blank=True)
    box4_text=models.TextField(verbose_name="Box 4 текст", default='Оруулаагүй', blank=True)
    box5_title=models.CharField(max_length=255, verbose_name="Box 5 гарчиг", default='Оруулаагүй', blank=True)
    box5_text=models.TextField(verbose_name="Box 5 текст", default='Оруулаагүй', blank=True)
    box6_title=models.CharField(max_length=255, verbose_name="Box 6 гарчиг", default='Оруулаагүй', blank=True)
    box6_text=models.TextField(verbose_name="Box 6 текст", default='Оруулаагүй', blank=True)
    box7_title=models.CharField(max_length=255, verbose_name="Box 7 гарчиг", default='Оруулаагүй', blank=True)
    box7_text=models.TextField(verbose_name="Box 7 текст", default='Оруулаагүй', blank=True)

    class Meta:
        verbose_name = '7 шалтгаан'
        verbose_name_plural = '7 шалтгаан'

class Settings(models.Model):
    logo=models.ImageField(upload_to="settings", verbose_name="Барилгын лого", default="settings/nh_logo.png", blank=True)
    phone=models.CharField(max_length=255, verbose_name="Холбоо барих утас",  blank=True, default='')
    mail=models.CharField(max_length=255, verbose_name="Компанийн э-мэйл хаяг",  blank=True, default='')
    location=models.CharField(max_length=255, verbose_name="Барилгын байршил",  blank=True, default='')
    facebook=models.CharField(max_length=255, verbose_name="Facebook хаяг",  blank=True, default='')
    instagram=models.CharField(max_length=255, verbose_name="Instagram хаяг",  blank=True, default='')
    twitter=models.CharField(max_length=255, verbose_name="Twitter хаяг",  blank=True, default='')


    class Meta:
        verbose_name = 'Сайтын тохиргоо'
        verbose_name_plural = 'Сайтын тохиргоо'

class PDFbrochure(models.Model):
    
    # subject=models.CharField(verbose_name="Сэдэв", max_length=255,  null=False, default=None)
    pdf=models.TextField(verbose_name="PDF link", blank=True, default='https://drive.google.com/file/d/1X7DCnk5kRnHOjiVvGe32TOWqAk2M2isu/view?ts=5f0287df')

    class Meta:
        verbose_name = 'PDF брошур'
        verbose_name_plural = 'PDF брошур'


class FeatureCard(models.Model):
    box1_title=models.CharField(max_length=255, verbose_name="Box 1 гарчиг", null=True, blank=True, default='Оруулаагүй')
    box1_text=models.TextField(verbose_name="Box 1 текст", null=True, blank=True, default='Оруулаагүй')
    box2_title=models.CharField(max_length=255, verbose_name="Box 2 гарчиг", null=True, blank=True, default='Оруулаагүй')
    box2_text=models.TextField(verbose_name="Box 2 текст", null=True, blank=True, default='Оруулаагүй')
    box3_title=models.CharField(max_length=255, verbose_name="Box 3 гарчиг", null=True, blank=True, default='Оруулаагүй')
    box3_text=models.TextField(verbose_name="Box 3 текст", null=True, blank=True, default='Оруулаагүй')
    box4_title=models.CharField(max_length=255, verbose_name="Box 4 гарчиг", null=True, blank=True, default='Оруулаагүй')
    box4_text=models.TextField(verbose_name="Box 4 текст", null=True, blank=True, default='Оруулаагүй')

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
    or_name=models.CharField(max_length=255, verbose_name="Байгууллагын нэр", null=True, blank=True, default='', unique=True)
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
    requested_time=models.DateField(verbose_name="Огноо", auto_now=True)
    
    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Холбоо барих хүсэлт"
        verbose_name_plural = "Холбоо барих хүсэлт жагсаалт"



class BuildingIntro(models.Model):
        
    title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="Оруулаагүй")
    text=models.TextField(verbose_name="Тайлбар", default='') 
    pic=models.ImageField(upload_to="Home/building_intro/", verbose_name="Зураг", default="settings/horizon10.jpg", blank=True)

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
    text_lil = models.CharField(max_length=255, verbose_name="Текст", blank=True, default='Default')
    title = models.CharField(max_length=255, verbose_name="Гарчиг", blank=True, default='Default')
    background_pic = models.ImageField(upload_to="Home", verbose_name="Зураг", default="settings/index.jpeg", blank=True)

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

class SubPage(models.Model):
    page_title = models.CharField(max_length=255, verbose_name="Хуудас гарчиг", null=True,  default="")
    lefty_title = models.CharField(max_length=255, verbose_name="Зүүн зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
    lefty_description = CKEditor5Field('Text', config_name='extends', blank=True)
    lefty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зүүн зурагтай - зураг", default='settings/index.jpeg', blank=True)

    notitledicon_left_title = models.CharField(max_length=255, verbose_name="NoTitledIcon left - Гарчиг", null=True, blank=True, default="Оруулаагүй")
    notitledicon_left_description = CKEditor5Field('Text', config_name='extends', blank=True)

    righty_title = models.CharField(max_length=255, verbose_name="Баруун зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
    righty_description = CKEditor5Field('Text', config_name='extends', blank=True)
    righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Баруун зурагтай - зураг", default='settings/index.jpeg', blank=True)
 
    
    notitledicon_right_title = models.CharField(max_length=255, verbose_name="NoTitledIcon right - Гарчиг", null=True, blank=True, default="Оруулаагүй")
    notitledicon_right_description = CKEditor5Field('Text', config_name='extends', blank=True)

    righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зураг том", default='settings/index.jpeg', blank=True)
    
    sign = models.CharField(max_length=255, null=True,  default="", editable=False)

    def __str__(self):
        return self.page_title

    class Meta:
        verbose_name = 'Дэд хуудас'
        verbose_name_plural = 'Дэд хуудас'

class SubPages_NoTitleIcon_Rightpic(models.Model):
    text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
    icon = models.ImageField(upload_to="Sub-pages/notitledicon", verbose_name="Зураг", default='', blank=True)
    organization=models.ForeignKey(SubPage, verbose_name="a", on_delete=models.CASCADE, default='')
    
    class Meta:
        verbose_name = 'No-Titled-Icon-right'
        verbose_name_plural = 'No-Titled-Icon-right'

class SubPages_NoTitleIcon_Leftpic(models.Model):
    text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
    icon = models.ImageField(upload_to="Sub-pages/notitledicon", verbose_name="Зураг", default='', blank=True)
    organization=models.ForeignKey(SubPage, verbose_name="a", on_delete=models.CASCADE, default='')
    
    class Meta:
        verbose_name = 'No-Titled-Icon-left'
        verbose_name_plural = 'No-Titled-Icon-left'

class SubPages_TitleIcon(models.Model):
    title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="")
    text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
    icon = models.ImageField(upload_to="Sub-pages/icon/notitledicon", verbose_name="Зураг", default='', blank=True)
    organization=models.ForeignKey(SubPage, verbose_name="a", on_delete=models.CASCADE, default='')
    
    
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'

class SubPages_Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="")
    text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
    icon = models.ImageField(upload_to="Sub-pages/icon/notitledicon", verbose_name="Зураг", default='', blank=True)
    organization=models.ForeignKey(SubPage, verbose_name="a", on_delete=models.CASCADE, default='')
    
    
    class Meta:
        verbose_name = 'Titled-Icon'
        verbose_name_plural = 'Titled-Icon'
    
class BuildingEnvironment(models.Model):
    title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="Манай орчин")
    text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")

    def __str__(self):
        return 'Барилын орчин өөрчлөх'

    class Meta:
        verbose_name = 'Барилгын орчин'
        verbose_name_plural = 'Барилгын орчин'
   
class BuildingEnvironmentPic(models.Model):
    pic = models.ImageField(upload_to="Home/Environemt", verbose_name="Зураг", default='', blank=True)
    organization=models.ForeignKey(BuildingEnvironment, verbose_name="a", on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'SLider Зураг'
        verbose_name_plural = 'Slider Зураг'

# # Sorry about HARD CODE :( Bo
# # It hurts my heart at the time 
# # HARD CODE START :'(
# class SubPageAboutUs(models.Model):
#     page_title = models.CharField(max_length=255, verbose_name="Хуудас гарчиг", null=True,  default="Бидний тухай")
#     lefty_title = models.CharField(max_length=255, verbose_name="Зүүн зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     lefty_description = CKEditor5Field('Text', config_name='extends', blank=True)
#     lefty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зүүн зурагтай - зураг", default='settings/index.jpeg', blank=True)

#     notitledicon_title = models.CharField(max_length=255, verbose_name="NoTitledIcon left - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     notitledicon_description = CKEditor5Field('Text', config_name='extends', blank=True)

#     righty_title = models.CharField(max_length=255, verbose_name="Баруун зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     righty_description = CKEditor5Field('Text', config_name='extends', blank=True)
#     righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Баруун зурагтай - зураг", default='settings/index.jpeg', blank=True)
 
    
#     notitledicon_title = models.CharField(max_length=255, verbose_name="NoTitledIcon right - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     notitledicon_description = CKEditor5Field('Text', config_name='extends', blank=True)

#     righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зураг том", default='settings/index.jpeg', blank=True)
    
#     def __str__(self):
#         return 'Өөрчлөх'

#     class Meta:
#         verbose_name = 'Бидний тухай'
#         verbose_name_plural = 'Бидний тухай'

# class SubPages_ABOUTUS_NoTitleIcon(models.Model):
#     text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
#     icon = models.ImageField(upload_to="Sub-pages/notitledicon", verbose_name="Зураг", default='', blank=True)
#     organization=models.ForeignKey(SubPageAboutUs, verbose_name="a", on_delete=models.CASCADE, default='')
    
#     class Meta:
#         verbose_name = 'No-Titled-Icon'
#         verbose_name_plural = 'No-Titled-Icon'

# class SubPages_ABOUTUS_TitleIcon(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="")
#     text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
#     icon = models.ImageField(upload_to="Sub-pages/icon/notitledicon", verbose_name="Зураг", default='', blank=True)
#     organization=models.ForeignKey(SubPageAboutUs, verbose_name="a", on_delete=models.CASCADE, default='')
    
    
#     class Meta:
#         verbose_name = 'Titled-Icon'
#         verbose_name_plural = 'Titled-Icon'


# class SubPageSecurity(models.Model):
#     page_title = models.CharField(max_length=255, verbose_name="Хуудас гарчиг", null=True,  default="Бидний тухай")
#     lefty_title = models.CharField(max_length=255, verbose_name="Зүүн зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     lefty_description = CKEditor5Field('Text', config_name='extends', blank=True)
#     lefty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зүүн зурагтай - зураг", default='settings/index.jpeg', blank=True)

#     notitledicon_title = models.CharField(max_length=255, verbose_name="NoTitledIcon left - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     notitledicon_description = CKEditor5Field('Text', config_name='extends', blank=True)

#     righty_title = models.CharField(max_length=255, verbose_name="Баруун зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     righty_description = CKEditor5Field('Text', config_name='extends', blank=True)
#     righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Баруун зурагтай - зураг", default='settings/index.jpeg', blank=True)
 
    
#     notitledicon_title = models.CharField(max_length=255, verbose_name="NoTitledIcon right - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     notitledicon_description = CKEditor5Field('Text', config_name='extends', blank=True)

#     righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зураг том", default='settings/index.jpeg', blank=True)
    
#     def __str__(self):
#         return 'Өөрчлөх'

#     class Meta:
#         verbose_name = 'Бидний тухай'
#         verbose_name_plural = 'Бидний тухай'

# class SubPages_SECURITY_NoTitleIcon(models.Model):
#     text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
#     icon = models.ImageField(upload_to="Sub-pages/notitledicon", verbose_name="Зураг", default='', blank=True)
#     organization=models.ForeignKey(SubPageAboutUs, verbose_name="a", on_delete=models.CASCADE, default='')
    
#     class Meta:
#         verbose_name = 'No-Titled-Icon'
#         verbose_name_plural = 'No-Titled-Icon'

# class SubPages_SECURITY_TitleIcon(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="")
#     text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
#     icon = models.ImageField(upload_to="Sub-pages/icon/notitledicon", verbose_name="Зураг", default='', blank=True)
#     organization=models.ForeignKey(SubPageAboutUs, verbose_name="a", on_delete=models.CASCADE, default='')
    
    
#     class Meta:
#         verbose_name = 'Titled-Icon'
#         verbose_name_plural = 'Titled-Icon'


# class SubPageStructure(models.Model):
#     page_title = models.CharField(max_length=255, verbose_name="Хуудас гарчиг", null=True,  default="Барилгын төлөвлөлт")
#     lefty_title = models.CharField(max_length=255, verbose_name="Зүүн зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     lefty_description = CKEditor5Field('Text', config_name='extends', blank=True)
#     lefty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зүүн зурагтай - зураг", default='settings/index.jpeg', blank=True)

#     notitledicon_title = models.CharField(max_length=255, verbose_name="NoTitledIcon left - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     notitledicon_description = CKEditor5Field('Text', config_name='extends', blank=True)

#     righty_title = models.CharField(max_length=255, verbose_name="Баруун зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     righty_description = CKEditor5Field('Text', config_name='extends', blank=True)
#     righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Баруун зурагтай - зураг", default='settings/index.jpeg', blank=True)
 
    
#     notitledicon_title = models.CharField(max_length=255, verbose_name="NoTitledIcon right - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     notitledicon_description = CKEditor5Field('Text', config_name='extends', blank=True)

#     righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зураг том", default='settings/index.jpeg', blank=True)
    
#     def __str__(self):
#         return 'Өөрчлөх'

#     class Meta:
#         verbose_name = 'Бидний тухай'
#         verbose_name_plural = 'Бидний тухай'

# class SubPages_STRUCTURE_NoTitleIcon(models.Model):
#     text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
#     icon = models.ImageField(upload_to="Sub-pages/notitledicon", verbose_name="Зураг", default='', blank=True)
#     organization=models.ForeignKey(SubPageAboutUs, verbose_name="a", on_delete=models.CASCADE, default='')
    
#     class Meta:
#         verbose_name = 'No-Titled-Icon'
#         verbose_name_plural = 'No-Titled-Icon'

# class SubPages_STRUCTURE_TitleIcon(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="")
#     text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
#     icon = models.ImageField(upload_to="Sub-pages/icon/notitledicon", verbose_name="Зураг", default='', blank=True)
#     organization=models.ForeignKey(SubPageAboutUs, verbose_name="a", on_delete=models.CASCADE, default='')
    
    
#     class Meta:
#         verbose_name = 'Titled-Icon'
#         verbose_name_plural = 'Titled-Icon'


# class SubPageUserExperience(models.Model):
#     page_title = models.CharField(max_length=255, verbose_name="Хуудас гарчиг", null=True,  default="Тав тух")
#     lefty_title = models.CharField(max_length=255, verbose_name="Зүүн зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     lefty_description = CKEditor5Field('Text', config_name='extends', blank=True)
#     lefty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зүүн зурагтай - зураг", default='settings/index.jpeg', blank=True)

#     notitledicon_title = models.CharField(max_length=255, verbose_name="NoTitledIcon left - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     notitledicon_description = CKEditor5Field('Text', config_name='extends', blank=True)

#     righty_title = models.CharField(max_length=255, verbose_name="Баруун зурагтай - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     righty_description = CKEditor5Field('Text', config_name='extends', blank=True)
#     righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Баруун зурагтай - зураг", default='settings/index.jpeg', blank=True)
 
    
#     notitledicon_title = models.CharField(max_length=255, verbose_name="NoTitledIcon right - Гарчиг", null=True, blank=True, default="Оруулаагүй")
#     notitledicon_description = CKEditor5Field('Text', config_name='extends', blank=True)

#     righty_pic = models.ImageField(upload_to="Sub-pages/about-us", verbose_name="Зураг том", default='settings/index.jpeg', blank=True)
    
#     def __str__(self):
#         return 'Өөрчлөх'

#     class Meta:
#         verbose_name = 'Бидний тухай'
#         verbose_name_plural = 'Бидний тухай'

# class SubPages_USEREXP_NoTitleIcon(models.Model):
#     text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
#     icon = models.ImageField(upload_to="Sub-pages/notitledicon", verbose_name="Зураг", default='', blank=True)
#     organization=models.ForeignKey(SubPageAboutUs, verbose_name="a", on_delete=models.CASCADE, default='')
    
#     class Meta:
#         verbose_name = 'No-Titled-Icon'
#         verbose_name_plural = 'No-Titled-Icon'

# class SubPages_USEREXP_TitleIcon(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Гарчиг", null=True, blank=True, default="")
#     text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True, default="")
#     icon = models.ImageField(upload_to="Sub-pages/icon/notitledicon", verbose_name="Зураг", default='', blank=True)
#     organization=models.ForeignKey(SubPageAboutUs, verbose_name="a", on_delete=models.CASCADE, default='')
    
    
#     class Meta:
#         verbose_name = 'Titled-Icon'
#         verbose_name_plural = 'Titled-Icon'
