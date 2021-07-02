from distutils.core import setup

setup(
    name='Django restframework datastore',
    version='0.0.1',
    description='Datastore built on DRF.',
    long_description=open('README.rst').read(),
    install_requires=['djangorestframework>=3.9'],
    packages=['datastore'],
    author='Albin Lindskog',
    author_email='albin@zerebra.com',
    url='https://github.com/albinlindskog/drf_datastore',
    zip_safe=True,
)