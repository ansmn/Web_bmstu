from django.contrib import admin
from .models import BugReport, FeatureRequest

class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title','project','task', 'status','priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True
    
class FeatureRequestInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title','project','task', 'status','priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title','project','task', 'status','priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title','project','task', 'status','priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')