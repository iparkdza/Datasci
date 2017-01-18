from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = [
    # Examples:
    url(r'^$', 'homepage.views.home', name='home'),
    #url(r'^$', 'register.views.login', name='login'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns = patterns('',(r'^$', 'homepage.views.home'),(r'^login/$', 'register.views.login'),(r'^register/$', 'register.views.regis'),(r'^logout/$', 'homepage.views.logout_page'),)