from django.db import models
from django_extensions.db.fields import RandomCharField



class Group(models.Model):
    
    group_name = models.CharField(max_length=500,verbose_name='խմբի անվանումը')
    group_slug = RandomCharField(length=8)

    def __str__(self):
        return self.group_name
    
    class Meta:
        managed = True
        verbose_name = 'խումբ'
        verbose_name_plural = 'խմբեր'


class Type(models.Model):

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=256,verbose_name='տիպ')
    group = models.ForeignKey(Group,on_delete=models.CASCADE,blank=True,verbose_name='խումբ')

    def __str__(self):
        return self.type
    
    class Meta:
        managed = True
        verbose_name = 'տիպ'
        verbose_name_plural = 'տիպեր'

class Post(models.Model):
    
    title = models.CharField(max_length=700,verbose_name="վերնագիր")
    type = models.ManyToManyField(Type,verbose_name='տիպ',blank=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,verbose_name='խումբ')
    img = models.ImageField(verbose_name="նկար")
    body = models.TextField(verbose_name="տեքստ")
    date = models.DateField(verbose_name="օր/ամիս/տարեթիվ",auto_now_add=True)
    
    def __str__(self):
        return self.title

    def delete(self,*args,**kwargs):
	    self.img.delete()
	    super().delete(*args,**kwargs)
	
    class Meta:
        managed = True
        verbose_name = 'գրառում'
        verbose_name_plural = 'գրառումներ'

class  Links(models.Model):

    link_name = models.CharField(max_length=256,verbose_name='անուն')
    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return self.link_name
    
    class Meta:
        managed = True
        verbose_name = 'հղում'
        verbose_name_plural = 'հղումներ'
