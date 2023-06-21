from django.contrib import admin
from .models import *

admin.site.site_header = "ZARAN"
admin.site.site_title = "ZARAN"
admin.site.index_title = "ZARAN"

admin.site.register(Projects)
admin.site.register(value)
admin.site.register(vlog)
admin.site.register(BlogArticle)

