from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from books import views as books_views
from library import views as library_views

router = routers.DefaultRouter()
router.register(r'books', books_views.BookViewSet)
router.register(r'borrowed-books', books_views.BorrowedBookViewSet, basename='library')
router.register(r'users', library_views.UserViewSet)
router.register(r'register', library_views.UserRegisterViewSet, basename='register')

# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token', views.obtain_auth_token)
]