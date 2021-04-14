# Django Cheat Sheet

terminal 

## CREATE VIRTUAL ENVIRONMENT AND START PROJECT

```cd desktop```

```mkdir day3```

```cd day3```

``` bash
virtualenv gifs_website
```

```bash
source gifs_website/bin/activate
````

```bash
pip3 install django
```

```bash
django-admin startproject gifs
```

```ls```

```cd gifs```

```bash 
python3 manage.py startapp info
```

```code . ```

```bash
python3 manage.py runserver
````


en VSCODE shift command p y abre la palette —> python select interpreter -> el que tenga el env que creaste

abrir settings—>install_app—>and add the app you just create ‘info.apps.InfoConfig’ ,


create urls.py inside the app folder
from django.urls import path

from . import views

urlpatterns= [
	path('',views.index, name='index')

]


then write a function in views.py

```python
def index(request):
	    return render(request, 'pages/index.html')
```


then urls.py en start projectname y add el nuevo url y la palabras include en from
```bash
from django.contrib import admin
from django.urls import path,include


path('', include('info.urls')),
```





