from django.urls import path
from .Controllers import Courses,Syllabus,Student

urlpatterns = [
    path('courses', Courses.ShowAll, name='course-list'),
    path('courses-create', Courses.CreateCourse, name='course-create'),
    path('course-update/<int:pk>', Courses.UpdateCourse, name='course-update'),
    path('courses-delete/<int:pk>',Courses.deleteCourse, name='course-delete'),
    path('syllabus', Syllabus.ShowAll, name='syllabus-list'),
    path('syllabus-create', Syllabus.CreateSyllabus, name='syllabus-create'),
    path('syllabus-update/<int:pk>', Syllabus.UpdateSyllabus, name='syllabus-update'),
    path('syllabus-delete/<int:pk>', Syllabus.deleteSyllabus, name='syllabus-delete'),
    path('student', Student.ShowAll, name='student-list'),
    path('student-create', Student.CreateStudent, name='student-create'),
    path('student-update/<int:pk>', Student.UpdateStudent, name='student-update'),
    path('student-delete/<int:pk>', Student.deleteStudent, name='student-delete'),
    path('student/course/<int:coursepk>', Student.getStudentFromCourse, name='student-course-get'),
    path('student/<int:pk>/syllabus/<int:syllabuspk>', Student.getStudentFromSyllabus, name='student-syllabus-get'),
    path('student/<int:pk>', Student.getStudentFromEnrollment, name='student-enrollment-get'),
]

