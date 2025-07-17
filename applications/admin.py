from django.contrib import admin
from .models import JobApplication
from django.utils.html import format_html



# @admin.register(JobApplication)
# class JobApplicationAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'job', 'email', 'phone', 'applied_at', 'cv_link')
#     list_filter = ('job', 'applied_at')
#     search_fields = ('full_name', 'email', 'phone')
#     def cv_link(self, obj):
#         if obj.resume:
#             return format_html('<a href="{}" target="_blank">Download</a>', obj.resume.url)
#         return "No File"

#     cv_link.short_description = "Resume"

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'applied_at', 'status', 'view_resume')
    list_filter = ('job', 'status')
    search_fields = ('user__username', 'job__title', 'user__email')
    ordering = ('-applied_at',)

    def view_resume(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank">Download</a>', obj.resume.url)
        return 'No CV Uploaded'

    view_resume.short_description = 'Resume'