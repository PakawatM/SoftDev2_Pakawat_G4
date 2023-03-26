from django.urls import path
from . import views

urlpatterns = [
    path('studytimetable', views.studyTimetable, name='study'),
    path('examtimetable', views.examTimetable, name='exam'),
    path('checksubject', views.checkSubject, name='check'),
    path('settingtimetable', views.settingtable, name='table'),
    path('add_subject', views.add_subject_request, name='add_subject'),
    path('students_planning_to_register', views.students_planning_to_register, name='students_planning_to_register'),
    path('number_of_students_registered', views.number_of_students_registered, name='number_of_students_registered'),
    path('verify/<int:subject_ID>', views.verify, name='verify'),
]