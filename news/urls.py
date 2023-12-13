from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import CategoryViewSet, AuthorViewSet, ArticleViewSet, UserSignupView, UserLoginView
from .views import *




router = DefaultRouter()
router.register(r'categories', TaxonomyViewSet)
router.register(r'authors', PostAuthorViewSet)
router.register(r'articles', PostDataViewSet)

   

urlpatterns = [
    path('', include(router.urls)),
    
   
    
    

]
