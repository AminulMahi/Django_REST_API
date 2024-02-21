from django.urls import path, include
from . import views
# from .views import StudentAPI
urlpatterns = [

    # path('student/', StudentAPI.as_view(), name='student'),
    # path('student_update/<int:id>/', views.update_student, name='student_update'),
    # path('student_delete/<int:id>/', views.delete_student, name='delete_student')


    path('', views.home),
    path('post_student', views.post_student, name='student'),
    path('update_student/<id>/', views.update_student),
    path('delete_student', views.delete_student, name='delete_student')
]
