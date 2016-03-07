from setuptools import find_packages, setup

VERSION = '0.1.1'
EXCLUDE_FROM_PACKAGES = ['controlcenter.stylus',
                         'controlcenter.images']

setup(
    name='django-controlcenter',
    version=VERSION,
    description='Set of widgets to build dashboards for your Django-project.',
    long_description='',
    url='https://github.com/byashimov/django-controlcenter',
    author='Murad Byashimov',
    author_email='byashimov@gmail.com',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
)
