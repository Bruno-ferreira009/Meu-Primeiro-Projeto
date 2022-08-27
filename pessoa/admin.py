from django.contrib import admin
from django.contrib.auth.models import User, Group

from pessoa.models import Pessoa

admin.site.unregister(Group)

admin.site.unregister(User)
admin.site.register(Pessoa)


