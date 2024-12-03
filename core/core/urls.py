from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('logout/', views.custom_logout, name="logout"),
    path('analyze/', views.analyze, name='analyze'),
    path('admin/', admin.site.urls),
    path('login/' , views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('', views.expenses, name='expenses'),
    path('update_expense/<id>', views.update_expense, name='update_expense'),
    path('delete_expense/<id>', views.delete_expense, name='delete_expense'),
]