from django.db import models

# Create your models here.
class DevelopTool(models.Model):
    name = models.CharField('이름',max_length=100)
    kind = models.CharField('종류',max_length=100)
    content = models.TextField('개발툴 설명')

    def __str__(self):
        return self.name