from django.urls import path
from user.views import SignupView, SigninView, SignoutView, MemberView #, check_code


# start with blog
#app_name="user"
urlpatterns = [
    # 用户注册
    path('signup', SignupView.as_view(), name='signup'),
    # 用户登录
    path('signin', SigninView.as_view(), name='signin'),
    # 用户退出
    path('signout', SignoutView.as_view(), name='signout'),
    # 查看某个用户信息
    path('member/<slug:username>', MemberView.as_view(), name='member'),

]