from django.contrib import admin
from .models import Profile, Department, Telephone, PositionType, Position, Assign


# Register your models here.
class PositionInline(admin.TabularInline):
    model = Position
    extra = 1


class AssignInline(admin.TabularInline):
    model = Assign
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['get_label_id']
    list_display = ['get_label_id', 'user', 'first_name', 'last_name', 'gender', 'birthday', 'national_id', 'email', 'mobile']
    list_filter = ['gender']
    search_fields = ['first_name', 'last_name', 'national_id', 'email', 'mobile']
    inlines = [PositionInline]
    
    def get_label_id (self, obj):
        return obj.id
    get_label_id.short_description = 'آیدی'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ['get_label_id']
    list_display = ['get_label_id', 'dep_title', 'dep_name', 'dep_address', 'level', 'super_dep']
    list_filter = ['dep_title', 'level', 'super_dep']
    search_fields = ['dep_name', 'dep_address']
    inlines = [PositionInline]

    def get_label_id (self, obj):
        return obj.id
    get_label_id.short_description = 'آیدی'


@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    readonly_fields = ['get_label_id']
    list_display = ['get_label_id', 'extension', 'complete_number', 'tel_address', 'description']
    list_filter = [ 'tel_address']
    search_fields = ['extension', 'complete_number', 'tel_address', 'description']
    inlines = [AssignInline]
    
    def get_label_id (self, obj):
        return obj.id
    get_label_id.short_description = 'آیدی'


@admin.register(PositionType)
class PositionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ['get_label_id']
    list_display = ['get_label_id', 'title', 'code', 'level']
    list_filter = ['level']
    search_fields = ['title', 'code']
    inlines = [PositionInline]
    
    def get_label_id (self, obj):
        return obj.id
    get_label_id.short_description = 'آیدی'


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    readonly_fields = ['get_label_id']
    list_display = ['get_label_id', 'position_type', 'dep', 'owner', 'duties']
    list_filter = ['dep__dep_title', 'owner__gender']
    search_fields = ['dep__dep_name', 'position_type__title', 'owner__last_name', 'owner__first_name']
    inlines = []

    def get_label_id (self, obj):
        return obj.id
    get_label_id.short_description = 'آیدی'


@admin.register(Assign)
class AssignAdmin(admin.ModelAdmin):
    readonly_fields = ('get_label_id',)
    list_display = ['get_label_id', 'position', 'tel', 'date']
    list_filter = ['position__dep__dep_title', 'date']
    search_fields = ['tel__extension', 'position__dep__dep_name', 'position__position_type__title', 'position__owner__first_name', 'position__owner__last_name', 'position__owner__gender']

    def get_label_id (self, obj):
        return obj.id
    get_label_id.short_description = 'آیدی'
    