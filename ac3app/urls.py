from django.conf.urls import patterns, url
from ac3app import views
from ac3app import emails
import AC3site.settings


urlpatterns = patterns('',
                       url(r'^$', views.index, name='login'),
                       url(r'^mainview/$', views.main_view, name='main_view'),
                       url(r'^profile/$', views.profile_view, name='profile'),
                       url(r'^login/$', views.login_view, name='login'),
                       url(r'^newpassword/$', views.new_pass, name='new_password'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^forgotpassword/$', emails.forgot_password_email, name='forgotpassword'),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
                                                                                   AC3site.settings.MEDIA_ROOT})
                       )

