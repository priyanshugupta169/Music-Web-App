from django.urls import path
from . import views
 
urlpatterns = [
   path('', views.index , name ='index'),
   path('index.html', views.index , name ='index'),
   path('register.html', views.register , name ='register'),
   path('login.html', views.login , name ='login'),
   path('contact.html', views.contactus , name ='contact'),
   path('logout.html', views.logout , name ='logout'),
   path('albums-store.html', views.albums , name ='album'),
   path('albums-store/<artist_name>', views.albums , name ='album'),
   path('Add_songs.html', views.Add_songs , name ='Addsongs'),
   path('Add_artist.html', views.Add_artist , name ='Addartist'),
   path('artist/<artist_name>', views.song , name ='song'),
   path('forgot_password.html', views.forgotpass , name ='forgotpass'),
   path('Change_Password.html', views.changepassword , name ='changepassword'),
  #  path('Add_songs.html', views.Add_songs , name ='Addsongs'),
 ]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)