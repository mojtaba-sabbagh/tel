from django.contrib import admin
from .models import UserProfile, Department, Telephone, PositionType, Position, Assign



# Register your models here.
@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'gender', 'birthday', 'national_id', 'email', 'mobile']
    list_filter = ['gender',]
    search_fields = ['first_name', 'last_name', 'national_id', 'email', 'mobile']




@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'address', 'level', 'super_dep']
    list_filter = ['title', 'level']
    search_fields = ['name']




@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    # readonly_fields = ('id',)
    # css = {
    #          'all': ('templates/css/admin-extra.css ',)
    #     }
    search_fields = ['extension']




@admin.register(PositionType)
class PositionTypeAdmin(admin.ModelAdmin):
    # readonly_fields = ('id',)
    # css = {
    #          'all': ('templates/css/admin-extra.css ',)
    #     }
    search_fields = ['title']




@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    # readonly_fields = ('id',)
    # css = {
    #          'all': ('templates/css/admin-extra.css ',)
    #     }
    list_filter = ('dep',)
    search_fields = ['dep__dep_name', 'owner__last_name', 'owner__first_name']




@admin.register(Assign)
class AssignAdmin(admin.ModelAdmin):
    # readonly_fields = ('id',)
    # css = {
    #          'all': ('templates/css/admin-extra.css ',)
    #     }
    search_fields = ['tel__extension', 'position__owner__last_name', 'position__dep__dep_name', 'position__owner__first_name']
