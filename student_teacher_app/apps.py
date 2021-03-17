from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class StudentTeacherAppConfig(AppConfig):
    name = 'student_teacher_app'

    def ready(self):
        import student_teacher_app.signals
