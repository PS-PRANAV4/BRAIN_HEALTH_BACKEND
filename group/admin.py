from django.contrib import admin

# Register your models here.
from .models import Comments,Accounts,DocCertificate,Post,Groups

# Register your models here.

admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(Groups)