from django.conf.urls import url
from .views import ViewSetItem,ViewSetVariant,ViewSetProperties,ItemRetrieve,LogDataCreateListViewSet,LogDataListViewSet#,ViewSetUser
urlpatterns = [
    #url(r'^user/$', ViewSetUser.as_view(), name='user-list'),
    url(r'^item/$', ViewSetItem.as_view(), name='item-list'),
    url(r'^item/(?P<pk>[0-9]+)/?$',ItemRetrieve.as_view(), name='retrieve-item'),
    url(r'^variant/$', ViewSetVariant.as_view(), name='variant-list'),
    url(r'^properties/$', ViewSetProperties.as_view(), name='variant-list'),
    url(r'^logdata/$', LogDataCreateListViewSet.as_view(), name='logdata-list-create'),
    url(r'^logdatafilter/$', LogDataListViewSet.as_view(), name='logdata-filter'),
    url(r'^logdatafilter/(?P<user>.+)/$', LogDataListViewSet.as_view(), name='logdata-list'),
]