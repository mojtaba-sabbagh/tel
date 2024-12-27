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
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
    title = models.CharField(max_length=255, blank=True, null=True, choices=TITLE_CHOICES, verbose_name='عنوان')
    name = models.CharField(max_length=255, verbose_name='نام')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='آدرس')
    level = models.IntegerField(default=0, verbose_name='سطح')
    super_dep = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='واحد های مرتبط')
    
    class Meta:
        ordering = ['title', 'name']
        verbose_name = 'واحد سازمانی'
        verbose_name_plural = 'واحدهای سازمانی'    
    
    def __str__(self):
        return f"{self.title} - {self.name}"


class Telephone(models.Model):
    extension = models.CharField(max_length=255, unique=True, verbose_name='افزونه')
    complete_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='تلفن کامل')
    tel_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='آدرس')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        ordering = ['extension', 'complete_number']
        verbose_name = "تلفن داخلی"
        verbose_name_plural = "تلفن‌های داخلی"
            
    def __str__(self):
        return self.complete_number


class PositionType(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    code = models.CharField(max_length=255, verbose_name="کد")
    level = models.IntegerField(default=0, verbose_name="سطح")

    class Meta:
        ordering = ['title']
        verbose_name = "نوع پست سازمانی"
        verbose_name_plural = "انواع پست های سازمانی"

    def __str__(self):
        return self.title


class Position(models.Model):
    position_type =  models.ForeignKey(PositionType, related_name='position_types', on_delete=models.CASCADE, verbose_name="نوع پست سازمانی")
    dep = models.ForeignKey(Department, related_name='deps', on_delete=models.CASCADE, verbose_name="واحد سازمانی")
    owner = models.ForeignKey(UserProfile, related_name='owners', on_delete=models.CASCADE, verbose_name="کاربر مسئول")
    duties = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name='وظایف')

    class Meta:
        ordering = ['dep', 'position_type', 'owner']
        verbose_name = "پست سازمانی"
        verbose_name_plural = "پست‌های سازمانی"

    def __str__(self):
        return f'{self.dep} - {self.position_type} - {self.owner}'


class Assign(models.Model):
    date = models.DateField(blank=True, null=True, verbose_name="تاریخ تخصیص")
    position = models.ForeignKey(Position, related_name='positions', on_delete=models.CASCADE, verbose_name="پست سازمانی")
    tel = models.ForeignKey(Telephone, related_name='tels', on_delete=models.CASCADE, verbose_name="شماره تلفن")

    class Meta:
        ordering = ['position', 'tel']
        verbose_name = "تخصیص تلفن"
        verbose_name_plural = "تخصیص تلفن‌ها"

    def __str__(self):
        return f'{self.position} - {self.tel}'
    