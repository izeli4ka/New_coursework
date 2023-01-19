from django.contrib import admin
from .models import User, News, Sale
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(User)
class users(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(News)
class news(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
        
@admin.register(Sale)
class sales(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True