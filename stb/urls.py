from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.models import User, Group
from import_server.models import Bill
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class BillViewSet(viewsets.ModelViewSet):
    model = Bill

admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'bills', BillViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
