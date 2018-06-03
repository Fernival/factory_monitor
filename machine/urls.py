from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from machine import views

router=DefaultRouter()
router.register(r'controler',views.ControlerViewSet)
router.register(r'processor',views.ProcessorViewSet)

app_name='machine'
urlpatterns=[
    url(r'',include(router.urls)),
    url(r'^controler/time/$',views.ControlerList.as_view()),
    url(r'^controler/time/latest/$',views.Controler_latest),
    url(r'^processor/time/$',views.ControlerList.as_view()),
    url(r'^processor/time/latest/$',views.Controler_latest),
]