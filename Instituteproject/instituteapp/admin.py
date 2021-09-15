from django.contrib import admin

from .models import CourseData

class AdminCourseData(admin.ModelAdmin):
    list_display = ['course_id','course_name','start_date','start_time','duration',
                    'trainer_name','trainer_exp','mode_of_training','fee']

admin.site.register(CourseData,AdminCourseData)