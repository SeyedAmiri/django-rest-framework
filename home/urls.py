from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

app_name = 'home'
urlpatterns = [
	path('', views.Home.as_view(), name='home'),  # endpoint
	path('questions/', views.QuestionListView.as_view()),
	path('question/create/', views.QuestionCreateView.as_view()),
	path('question/update/<int:pk>/', views.QuestionUpdateView.as_view()),
	path('question/delete/<int:pk>/', views.QuestionDeleteView.as_view()),

]