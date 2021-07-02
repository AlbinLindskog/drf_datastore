Django Restframework DataStore
------------------------------
Bare-bones Django app to store unstructured JSON-data, no validation, no formatting, no querying.
Designed to store non-critical data used for a SPA frontend.::

    import requests

    >>> requests.put('http://localhost:8000/datastore/user_preferences/', json={'vegan': false})
    {'vegan': false}

    >>> requests.get('http://localhost:8000/datastore/user_preferences/')
    {'vegan': false}

Setup
^^^^^
Simply add datastore to your ``INSTALLED_APPS`` and base url-config .::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'datastore,
        ...
    ]

    urlpatterns = [
        ...
        path('datastore/', include('datastore.urls', namespace='datastore')),
        ...
    ]

This will make the datastore API available at /datastore/<key>/.

Development
^^^^^^^^^^^
To run the tests, clone the repository, setup the virtual environment, and run
the tests.::

    # Setup the virtual environment
    $ virtualenv test_env
    $ source test_env/bin/activate
    $ pip3 install -r test_requirements.txt

    # Run the tests
    $ cd tests
    $ python3 manage.py test
