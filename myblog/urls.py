from django.urls import path
from myblog.apps import MyblogConfig
from myblog.views import MyblogListView, MyblogCreateView, MyblogDetailView, MyblogUpdateView, MyblogDeleteView

app_name = MyblogConfig.name

urlpatterns = [

    path("create", MyblogCreateView.as_view(), name="create"),
    path("list", MyblogListView.as_view(), name='list'),
    path("view/<int:pk>/", MyblogDetailView.as_view(), name='view'),
    path("edit/<int:pk>/", MyblogUpdateView.as_view(), name='edit'),
    path("delete/<int:pk>/", MyblogDeleteView.as_view(), name="delete"),
]
