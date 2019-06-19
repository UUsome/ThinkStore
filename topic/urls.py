from django.urls import path
from topic.views import IndexView, NodeView, TopicView, NodeLinkView, RecentView, NewTopicView, MarkdownPreView, \
    MyFavoriteNodeView, MyFavoriteTopicView, MyFollowingView,test


# start with blog
#app_name="topic"
urlpatterns = [
    # http://localhost:8000/blog/1
    # 首页，默认是最热节点 最多30条
    path('', IndexView.as_view(), name='index'),
    # 发布新主题
    path('new', NewTopicView.as_view(), name='new'),
    # 主题查看
    path('t/<slug:topic_sn>', TopicView.as_view(), name='topic'),
    # 我收藏的节点
    path('my/nodes', MyFavoriteNodeView.as_view(), name='my_nodes'),
    # 我收藏的节点
    path('my/nodes', MyFavoriteNodeView.as_view(), name='my_nodes'),
    # 我收藏的主题
    path('my/topics', MyFavoriteTopicView.as_view(), name='my_topics'),
    # 我关注的人的信息
    path('my/following', MyFollowingView.as_view(), name='my_following'),
    #测试html bootsrap样式
    path('test', test, name='test'),
]