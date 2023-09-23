from django.urls import re_path as url
from django_passbook.views import register_pass, latest_version, registrations, log

urlpatterns = [
    url(r'^v1/devices/(?P<device_library_id>.+)/registrations/(?P<pass_type_id>[\w\.\d]+)/(?P<serial_number>.+)$', register_pass),
    url(r'^v1/devices/(?P<device_library_id>.+)/registrations/(?P<pass_type_id>[\w\.\d]+)$', registrations),
    url(r'^v1/passes/(?P<pass_type_id>[\w\.\d]+)/(?P<serial_number>.+)$', latest_version),
    url(r'^v1/log$', log)
]
