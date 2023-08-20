#他のファイルから何かをちょこっとずつ追加する行です。 
#なので色んなファイルから必要な部分をコピペする代わり
from django.conf import settings
from django.db import models
from django.utils import timezone

#この行が今回のモデルを定義します (これが オブジェクト です)。
#classはオブジェクトを定義,Post はモデルの名前
#models.Model はポストがDjango Modelだという意味で、Djangoが、
#これはデータベースに保存すべきものだと分かるようにしている
class Post(models.Model):
    #これは他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #models.CharField – 文字数が制限されたテキストを定義するフィールド
    title = models.CharField(max_length=200)

    #models.TextField – これは制限無しの長いテキスト用
    text = models.TextField()

    #日付と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #ブログを公開するメソッドそのもの
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #ポストのタイトルのテキスト（string）が返ってくる
    def __str__(self):
        return self.title