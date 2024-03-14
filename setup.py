from distutils.core import setup

version = __import__('django_passbook').__version__

setup(
    name='django-passbook',
    version='1.0.1',
    author='Aleksei Tcelishchev',
    author_email='casualuser@gmail.com',
    packages=['django_passbook', 'django_passbook.migrations'],
    url='http://github.com/casualuser/django-passbook/',
    license=open('LICENSE.txt').read(),
    description='Django Passbook server app ',
    long_description=open('README.md').read(),

    download_url='http://pypi.python.org/packages/source/D/django-passbook/django-passbook-%s.tar.gz' % version,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
