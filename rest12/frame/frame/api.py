from django.db import router
from rest_framework import routers
from menu import views 



router = routers.DefaultRouter()

router.register(r'books', views.BookViewset)
router.register(r'libusers', views.libuser)

