# django-ogp-view
すべてのViewクラスにOGP (The Open Graph protocol)を適応させるライブラリです。  
view classに継承させることで、metaタグを簡単に設定できます。  
画面ごとにカスタマイズすることもできます。  
SEO (Search Engine Optimization)対策に最適です。  

## 導入
1. ライブラリをインストールする。
```sh
pip install django-ogp-view # まだ未登録なので実施不可
pip install git+https://github.com/taogya/DjangoOgpView.git
```
1. settings.pyに以下を追加する。
```python
INSTALLED_APPS = [
    :
    'django_ogp'
]
OGP_SITE_PROPERTY_MODEL = 'django_ogp.OgpSiteProperty'
OGP_LOCALE_MASTER_MODEL = 'django_ogp.OgpLocaleMaster'
OGP_MIMETYPE_MASTER_MODEL = 'django_ogp.OgpMimeTypeMaster'
```
1. migrateを行う。
```python
python manage.py makemigrations
python manage.py migrate
```
1. masterデータを作成する。
```python
python manage.py shell
from django_ogp.models import create_master

create_master()
```
1. OGP用のプロパティを設定する。
- OgpSiteProperty  
サイト内共通のプロパティ。
- OgpBasicProperty  
ページごとのプロパティ。
- OgpCustomProperty  
カスタムプロパティ。  
JSONで指定する。  
JSONについて, keyはpropertyの名称, valueはcontentの値で指定する。  
1. ViewにOgpViewMixinを継承し, 割り当てるプロパティのレコードを割り当てる。
```python
from django.views import View
from django_ogp.view import OgpViewMixin
from django_ogp.models import OgpBasicProperty

class YourView(View, OgpViewMixin):
    ogp = OgpBasicProperty.objects.first()
    :
```
1. 以下のようにhtmlファイルにdjango_ogp用のタグを追加する。
```html
{% load django_ogp %}
<!DOCTYPE html>
<html lang="en" prefix="{{ view.ogp_global_prefix }}">
  <head prefix="{{ view.ogp_prefix }}">
    {% add_ogp_meta %}
    :
```