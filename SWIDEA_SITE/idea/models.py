from django.db import models
from developTool.models import DevelopTool  # DevelopTool 모델을 import
# Create your models here.

class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey('developTool.DevelopTool', on_delete=models.CASCADE, related_name='ideas')  # DevelopTool과의 관계 추가
    is_liked = models.BooleanField(default=False)  # 찜하기 여부
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜 (정렬용)

    def __str__(self):
        return self.title
