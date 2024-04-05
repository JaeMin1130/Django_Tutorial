from django.urls import path
from . import views

urlpatterns = [
    # url : "/polls/"
    path("", views.index, name="index"),
    # url : "/polls/5/"
    path("<int:question_id>/", views.detail, name="detail"),
    # url : "/polls/5/results/"
    path("<int:question_id>/results/", views.results, name="results"),
    # url : "/polls/5/vote/"
    path("<int:question_id>/vote/", views.vote, name="vote")
]
