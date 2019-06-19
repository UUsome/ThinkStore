from django.urls import path
from .views import CaseAdd, caseList , caseDiscrib, IdeaAdd,ideaDetil


# start with blog
#app_name=""
urlpatterns = [
    # 添加框架系统
    path('caseadd', CaseAdd.as_view(), name='caseadd'),
    # 查看框架系统
    path('caselist', caseList , name="caselist" ),
    # 添加方案
    path('ideaadd/<int:id>', IdeaAdd.as_view(), name="ideaadd"),
    # 查看框架详情
    path('casediscrib/<int:id>', caseDiscrib, name="casediscrib"),
    # 查看方案详情
    path('ideadetil/<int:ctid>/<int:itid>', ideaDetil, name="ideadetil"),
    # path('ideadetil/<int:itid>', ideaDetil, name="ideadetil"),

]