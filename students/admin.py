from django.contrib import admin
from .models import Estudent, Representative, Receipts


# Register your models here.
# admin.site.register(Estudent)
# admin.site.register(Representative)
# admin.site.register(Receipts)


@admin.register(Estudent)
class EstudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'fn',
                    'representative', 'kinship')
    fields = ['id', ('first_name', 'last_name'), ('fn', 'sex'), 'address', ('phone', 'email'),
              ('representative', 'kinship')]


@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'fn', 'phone')


@admin.register(Receipts)
class ReceiptsAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_period', 'student',
                    'grade', 'representative')
