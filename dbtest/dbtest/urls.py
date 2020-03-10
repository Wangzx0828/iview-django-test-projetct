from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView //注意加上这句

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name="index.html")),
]