import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name = 'django-localflavor-il',
    version = '1.0',
    description = 'Country-specific Django helpers for Israel.',
    long_description = README,
    author = 'Django Software Foundation',
    author_email = 'foundation@djangoproject.com',
    license='BSD',
    url = 'https://github.com/django/django-localflavor-il',
    packages = ['django_localflavor_il'],
    include_package_data = True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django>=1.4',
    ],
    test_suite = 'setuptest.setuptest.SetupTestsSuite',
    tests_require = (
        'django-setuptest',
        'argparse'),
)
