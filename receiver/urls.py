from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from receiver import views

urlpatterns = [
    path('records/', views.RecordList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
