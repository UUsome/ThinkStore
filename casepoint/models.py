from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

##添加的架构
#类型表 ：   id，类型名称，删除字段
class CaseType(models.Model):
    name = models.CharField(max_length=64,verbose_name='框架分类')
    info = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'说明')
    isValid = models.IntegerField(default=1,verbose_name='删除字段')
    # 定义静态方法
    def  __str__(self):
        return self.name


#框架标题 :  id,标题名称，说明，创建者，查看权限，删除字段，添加时间,最后更新时间
class CaseTitle(models.Model):
    caseType = models.ForeignKey(CaseType, on_delete=models.CASCADE,null=False,verbose_name='主题分类')
    title = models.CharField(max_length=64,unique=True,verbose_name='主题名称')
    info = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'说明')
    viewPermissions =models.IntegerField(default=1,verbose_name='查看权限')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,verbose_name='用户')
    is_valid = models.IntegerField(default=1,verbose_name='删除字段')
    create_time=models.DateTimeField(auto_now=True,verbose_name="主题创建时间")
    update_time=models.DateTimeField(auto_now=True,verbose_name="主题更新时间")

    def  __str__(self):
        return self.title

    def __unicode__(self):
        return (u'%d,%d,%s') % (self.id, self.caseType, self.title)


# 框架步骤 ： id,框架id，框架步骤内容，说明,父ID
class CaseContent(models.Model):
    title = models.ForeignKey(CaseTitle, on_delete=models.CASCADE, null=False,verbose_name='框架id')
    Contents = models.CharField(max_length=64,unique=False,verbose_name='框架内容')
    info = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'说明')
    parentId = models.IntegerField(default=0,verbose_name='父ID')
    # 定义表注释
    class Meta:
        verbose_name='case内容'
        verbose_name_plural=verbose_name


    def __str__(self):
        return  self.Contents


##内容输入
#框架标题 :  id,标题名称，说明，创建者，查看权限，删除字段，添加时间,最后更新时间
class CaseIdeaTitle(models.Model):
    title = models.CharField(max_length=64,unique=False,verbose_name='主题名称')
    caseTitle = models.ForeignKey(CaseTitle, on_delete=models.CASCADE, null=False, verbose_name='case标题')
    info = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'说明')
    viewPermissions =models.IntegerField(default=1,verbose_name='查看权限')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,verbose_name='用户')
    isValid = models.IntegerField(default=1,verbose_name='删除字段')
    createTime=models.DateTimeField(auto_now=True,verbose_name="主题创建时间")

    class  Meta:
        verbose_name='方案主题'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title


# 框架步骤输入 ： id,框架id，框架步骤内容，说明,父ID
class CaseIdeaContent(models.Model):
    caseContent = models.ForeignKey(CaseContent, on_delete=models.CASCADE, null=False, verbose_name='case内容')
    title = models.ForeignKey(CaseIdeaTitle, on_delete=models.CASCADE,null=False,verbose_name='框架id')
    contents = models.CharField(max_length=64,unique=False,verbose_name='框架内容')
    info = models.TextField(max_length=200, null=True, blank=True, verbose_name=u'说明')
    parentI_id = models.IntegerField(default=0,verbose_name='父ID')
    createTime=models.DateTimeField(auto_now=True,verbose_name="主题创建时间")
    updateTime=models.DateTimeField(auto_now=True,verbose_name="主题更新时间")

    class  Meta:
        verbose_name='方案内容'
        verbose_name_plural=verbose_name

    def  __str__(self):
        return  self.contents

