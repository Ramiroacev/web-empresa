from django.urls import path
from . import views


urlpatterns = [
    # Paths del core
    path('blog/', views.blog, name="blog"),
    path('blog/category/<int:category_id>/', views.category, name="category"),
]
