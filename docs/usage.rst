=====
Usage
=====

To use django-pwny in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'pwny.apps.PwnyConfig',
        ...
    )

Add django-pwny's URL patterns:

.. code-block:: python

    from pwny import urls as pwny_urls


    urlpatterns = [
        ...
        url(r'^', include(pwny_urls)),
        ...
    ]
