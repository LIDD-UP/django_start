from django.db import models
# import choice

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20,verbose_name="英雄姓名") #
    gender = (
        ('0','男'),
        ('1','女'),
        ('2','秘密')
    )
    hsex = models.IntegerField(choices=gender,default=2,blank=True,verbose_name='性别')
    hcomment = models.CharField(max_length=200,verbose_name="英雄评论")
    # bookInfo和hearoinfo 是一对多关系
    hbook = models.ForeignKey("BookInfo")