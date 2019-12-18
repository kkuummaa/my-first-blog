from django.conf import settings
from django.db import models
from django.utils import timezone

# ブログポストのモデル作るぜ〜
# クラスはオブジェクトを定義してますよというキーワード
class Post(models.Model): #models.ModelはPostがDjango Modelだという意味。これにより、Djangoが、これはデータベースに保存すべきものだとわかるようにしている。
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログを公開するメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title