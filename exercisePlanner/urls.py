from django.urls import path
from .views import HomePageView, AddPostViewExercise, SeeExercises, DeleteExercisePost
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('postExercise/<int:pk>', AddPostViewExercise.as_view(), name='postExercise'),  # url to my create request page
    path('exercises/<int:pk>', SeeExercises.as_view(), name='exercises'),  # url to see the created requests
    path('delete/<int:pk>', DeleteExercisePost.as_view(), name='delete'),  # path to delete requests done by user
]


