from django.conf import settings

PASSBOOK_CERT = getattr(settings, 'PASSBOOK_CERT', '')
PASSBOOK_CERT_KEY = getattr(settings, 'PASSBOOK_CERT_KEY', '')
PASSBOOK_CERT_PASS = getattr(settings, 'PASSBOOK_CERT_PASS', '')
PASSBOOK_CHAIN_CERT = getattr(settings, 'PASSBOOK_CHAIN_CERT', '')
