[jp](README.md)

# django-ogp-view
A library that adapts OGP (The Open Graph protocol) to View classes.  
By inheriting the ViewMixin of this library, the implementation of the ogp meta tag can be simplified.  
You can also customize each screen.  
It is also ideal for SEO (search engine optimization) measures.  

## Introduction
1. Install the library.
    ```sh
    pip install django-ogp-view
     or
    pip install git+https://github.com/taogya/DjangoOgpView.git
    ```
1. Add the following to `settings.py`.
    ```python
    INSTALLED_APPS = [
        :
        'django_ogp'
    ]
    OGP_SITE_PROPERTY_MODEL = 'django_ogp.OgpSiteProperty'
    OGP_LOCALE_MASTER_MODEL = 'django_ogp.OgpLocaleMaster'
    OGP_MIMETYPE_MASTER_MODEL = 'django_ogp.OgpMimeTypeMaster'
    ```
1. do migrate.
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```
1. Set properties for OGP.
    - OgpSiteProperty  
    Site common properties.
    - OgpBasicProperty  
    Properties per page.
    - OgpCustomProperty  
    Custom properties.  
    Specify in JSON.  
    For JSON, specify the key as the name of the property and the value as the content value.  
1. Inherit OgpViewMixin to View and assign the record of the property to be assigned.
    ```python
    from django.views import View
    from django_ogp.view import OgpViewMixin
    from django_ogp.models import OgpBasicProperty

    class YourView(View, OgpViewMixin):
        ogp = OgpBasicProperty.objects.first()
        :
    ```
1. Add a tag for django_ogp to the html file as follows.
    ```html
    {% load django_ogp %}
    <!DOCTYPE html>
    <html lang="en" prefix="{{ view.ogp_global_prefix }}">
    <head prefix="{{ view.ogp_prefix }}">
        {% add_ogp_meta %}
        :
    ```

## Models
![django_ogp_er_](/resources/django_ogp_er.png)

## 補足
- [Migration file](django_ogp/migrations/0001_initial.py) contains a master data automatic generation script.  
If there is unnecessary data, please delete it on the administrator screen or modify the [migration file](django_ogp/migrations/0001_initial.py).
- The following models are `swappable` models.
    - OgpSiteProperty
    - OgpLocaleMaster
    - OgpMimeTypeMaster
