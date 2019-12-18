from django.contrib import admin
from .models import Post

# Register your models here.
# 登録したモデルは、Adminnページ（管理画面）で見えるようになる。
admin.site.register(Post)
