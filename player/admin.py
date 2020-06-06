from django.contrib import admin
from .models import Accounts,Contact,Songs,Artist
# Register your models here.
admin.site.register(Accounts)
admin.site.register(Contact)
admin.site.register(Songs)
admin.site.register(Artist)