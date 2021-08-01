from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from.views import HomeView,ArticlePostView,AddPostView,UpdatePostView,DeletePostView



urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticlePostView.as_view(),name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)