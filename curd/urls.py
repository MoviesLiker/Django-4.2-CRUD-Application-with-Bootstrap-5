from django.urls import path

from . import views

app_name = "curd"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("<int:id>", views.edit, name="edit"),
    path("curd-submit", views.curd_submit, name="curd_submit"),
    path("edit-submit/<int:id>", views.edit_submit, name="edit_submit"),
    path("curd-delete/<int:id>", views.curd_delete, name="curd_delete"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]