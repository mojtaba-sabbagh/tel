from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'مرد'),
        ('F', 'زن'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='حساب کاربری')
    profile = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='عکس پروفایل')
    first_name = models.CharField(max_length=255, verbose_name='نام')
    last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES, verbose_name='جنسیت')
    birthday = models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')
    national_id = models.CharField(max_length=10, unique=True, blank=True, null=True, verbose_name='کدملی')
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name='ایمیل')
    mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name='تلفن همراه')


    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "کاربر"
        verbose_name_plural = "مدیریت کاربران"
        
        
    def __str__(self):
        return f'آیدی: {self.id}'




class Department(models.Model):
    TITLE_CHOICES = (
        ('معاونت', 'معاونت'),
        ('مدیریت', 'مدیریت'),
        ('دانشکده', 'دانشکده'),
        ('گروه', 'گروه'),
        ('اداره', 'اداره'),
        ('دبیرخانه', 'دبیرخانه'),
        ('حوزه', 'حوزه'),
        ('مرکز', 'مرکز'),
        ('کمیته', 'کمیته'),
        ('شورا', 'شورا'),
        ('سرای', 'سرای دانشجوی'),
        ('گیت', 'گیت'),
    )
    dep_title = models.CharField(max_length=255, blank=True, null=True, choices=TITLE_CHOICES)
    dep_name = models.CharField(max_length=255)
    dep_address = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(default=0)
    super_dep = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="the related dep")
    

    class Meta:
        ordering = ['dep_title', 'dep_name']
        verbose_name = "واحد سازمانی"
        verbose_name_plural = "واحدهای سازمانی"
        
    
    def __str__(self):
        return f'آیدی: {self.id}'




class Telephone(models.Model):
    extension = models.CharField(max_length=255, unique=True)
    complete_number = models.CharField(max_length=255, blank=True, null=True)
    tel_address = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        ordering = ['extension']
        verbose_name = "تلفن داخلی"
        verbose_name_plural = "تلفن‌های داخلی"
        
    
    def __str__(self):
        return f'آیدی: {self.id}'




class PositionType(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    level = models.IntegerField(default=0)


    class Meta:
        ordering = ['title']
        verbose_name = "نوع پست سازمانی"
        verbose_name_plural = "انواع پست های سازمانی"


    def __str__(self):
        return f'آیدی: {self.id}'




class Position(models.Model):
    position_type =  models.ForeignKey(PositionType, related_name='position_types', on_delete=models.CASCADE, verbose_name="the related position type")
    dep = models.ForeignKey(Department, related_name='deps', on_delete=models.CASCADE, verbose_name="the related dep")
    owner = models.ForeignKey(UserProfile, related_name='owners', on_delete=models.CASCADE, verbose_name="the related profile")
    duties = models.CharField(max_length=255, blank=True, null=True, default='')


    class Meta:
        ordering = ['dep', 'position_type', 'owner']
        verbose_name = "پست سازمانی"
        verbose_name_plural = "پست‌های سازمانی"

    
    def __str__(self):
        return f'آیدی: {self.id}'




class Assign(models.Model):
    date = models.DateField(blank=True, null=True)
    position = models.ForeignKey(Position, related_name='positions', on_delete=models.CASCADE, verbose_name="the related pos")
    tel = models.ForeignKey(Telephone, related_name='tels', on_delete=models.CASCADE, verbose_name="the related tel")


    class Meta:
        ordering = ['tel']
        verbose_name = "تخصیص تلفن"
        verbose_name_plural = "تخصیص تلفن‌ها"


    def __str__(self):
        return f'آیدی: {self.id}'
