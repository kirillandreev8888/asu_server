from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.notfound),
    path('auth/', views.auth),
    path('404/', views.notfound),
    path('groups/', views.groups),
    path('groups/api-editgrouplist/', views.editgrouplist),
    path('groups/api-loadgrouplessons/', views.loadgroups),
    path('groups/api-editlesson/', views.editlesson),
    re_path(r'^groups/(?P<id>\d+)/$', views.groupedit)
    # re_path(r'^.*$', RedirectView.as_view(url='404/', permanent=False), name='index')

]
