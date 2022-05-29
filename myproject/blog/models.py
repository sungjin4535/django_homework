from email.quoprimime import body_check
from turtle import title
from django.db import models

class Blog(models.Model):  #모델 : 엑셀의 라벨과 같은 부분
    title = models.CharField(max_length=50)  
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self): 
        return self.title

    def summary(self):   #글자 수 제한하는 함수
        return self.body[:100]
        
#모델 만들었다고 장고가 바로 인식할 수는 없음
#터미널에서 python3 manage.py makemigrations
#python3 manage.py migrate
# Create your models here.
