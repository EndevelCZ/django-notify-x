from django.urls import re_path

from notify import views as nf

app_name = 'notifications'


urlpatterns = [
    re_path(r'^all/$', nf.notifications, name="all"),
    re_path(r'^api/update/$', nf.notification_update, name="update"),
    re_path(r'^mark/$', nf.mark, name='mark'),
    re_path(r'^mark-all/$', nf.mark_all, name='mark_all'),
    re_path(r'^delete/$', nf.delete, name='delete'),
    re_path(r'^rdr/(?P<notification_id>[\d]+)/$', nf.read_and_redirect,
        name='read_and_redirect'),
]
