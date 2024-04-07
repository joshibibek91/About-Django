#How to display contents in server webpage

1. Go to views.py from created app "home"

2. import httpresponse from django.http

3. define a function home there

4. return httpresponse as your message

5. views.py looks like following 

    from django.shortcuts import render
    from django.http import HttpResponse



    def home(request):
        return HttpResponse("Hey I am a Django Server")

6. go to urls.py from core folder

7. create a path making blank url for home, with home function from views giving a name eg home. 

8. Don't forget to import all from views. The url window looks like following.

    from django.contrib import admin
    from django.urls import path
    from Home.views import *

    urlpatterns = [
        path('', home, name='home'),
        path('admin/', admin.site.urls),
    ]

9. Now refresh the server and you will find a server page with message "Hey I am a Django server" in top right corner.