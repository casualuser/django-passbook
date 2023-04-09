from django.contrib import admin
from django_passbook.models import Pass, Registration, Log
from django_passbook import settings
from apns_python import Alert, APS, Payload, Headers, Client


def push_update(modeladmin, request, queryset):
    for r in queryset.all():
        # FIXME: use different certificates for different stores

        headers = Headers(
            custom_fields={"Content-Type": "application/json; charset=utf-8"})

        client = Client(
            push_mode='prd',
            secure=True,
            cert_chain_location=settings.PASSBOOK_CHAIN_CERT,
            cert_location=(settings.PASSBOOK_CERT, settings.PASSBOOK_CERT_KEY),
            cert_password=settings.PASSBOOK_CERT_PASS)

        result = client.send(r.push_token, headers, Payload())


push_update.short_description = "Send a push notification to update Pass"


class RegistrationAdmin(admin.ModelAdmin):
    actions = [push_update]

admin.site.register(Pass)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Log)
