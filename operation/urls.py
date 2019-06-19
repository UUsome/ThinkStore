from django.urls import path
from operation.views import TopicVoteView, FavoriteTopicView, ThanksTopicView, FavoriteNodeView, FollowingView, \
    BlockView, SettingView, PhoneSettingView, EmailSettingView, SendActivateCodeView, ActivateEmailView,\
    AvatarSettingView, PasswordSettingView, DailyMissionView, DailyRandomBalanceView, BalanceView


# start with blog
#app_name="operation"
urlpatterns = [
    # 主题投票
    path('topic/vote', TopicVoteView.as_view(), name='topic_vote'),
    # 主题收藏
    path('topic/favorite', FavoriteTopicView.as_view(), name='favorite_topic'),
    # 主题感谢
    path('topic/thanks', ThanksTopicView.as_view(), name='thanks_topic'),
    # 节点收藏
    path('node/favorite', FavoriteNodeView.as_view(), name='favorite_node'),
    # 用户设置
    path('settings', SettingView.as_view(), name='settings'),
    # 用户头像设置
    path('settings/avatar', AvatarSettingView.as_view(), name='settings_avatar'),
    # 用户手机设置
    path('settings/phone', PhoneSettingView.as_view(), name='settings_phone'),
    # 用户Email设置
    path('settings/email', EmailSettingView.as_view(), name='settings_email'),
    # 密码修改
    path('settings/password', PasswordSettingView.as_view(), name='settings_password'),
    # 发送随机码地址
    path('activate', SendActivateCodeView.as_view(), name='activate'),
    # 用户邮箱激活链接
    path('activate/<slug:code>', ActivateEmailView.as_view(), name='activate_email'),
    # Following 动作
    path('following/<slug:username>', FollowingView.as_view(), name='following'),
    # Block 动作
    path('block/<slug:username>', BlockView.as_view(), name='block'),
    # 每日金币奖励
    path('mission/daily', DailyMissionView.as_view(), name='daily_mission'),
    # 随机生成金钱接口
    path('mission/daily/redeem', DailyRandomBalanceView.as_view(), name='daily_random_balance'),
    # 用户金钱
    path('balance', BalanceView.as_view(), name='balance'),
]
