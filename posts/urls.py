from django.urls import path 
from posts import views


urlpatterns = [
    path('', views.PostView.as_view(), name='post_view'),
    path('feed/', views.FeedView.as_view(), name='feed_view'), # 추가
    path('<int:post_id>/', views.PostDetailView.as_view(), name='post_detail_view'),
    # path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail_view'),
    path('<int:post_id>/comment/', views.CommentView.as_view(), name='comment_view'),
    path('<int:post_id>/comment/<int:comment_id>', views.CommentDetailView.as_view(), name='comment_detail_view'),
    path('<int:post_id>/like/', views.LikeView.as_view(), name='like_view'),

]