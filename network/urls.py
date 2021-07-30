
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("all_posts", views.all_posts, name="all_posts"),
    #path("all_posts_2", views.all_posts, name="all_posts_2"),
    path("posts", views.compose, name="compose"),
    path("comment/<int:post_id>", views.comment, name="comment"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("edit_2/<int:post_id>", views.edit_2, name="edit_2"),
    path("comment_add/<int:post_id>", views.comment_add, name="comment_add"),
    path("profile/<int:creator_id>", views.profile, name="profile"),
    path("follower_add/<int:following_id>", views.follower_add, name="follower_add"),
    path("follower_del/<int:following_id>", views.follower_del, name="follower_del"),
    path("follower_index", views.follower_index, name="follower_index")
]
