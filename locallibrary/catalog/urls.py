from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
     path('accounts/', include('django.contrib.auth.urls')),

]
