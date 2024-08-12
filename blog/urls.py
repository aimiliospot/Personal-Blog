from django.urls import path
from . import views
from .views import IndexView, AboutView, ContactView, UniquePostView, CommentSubmitView, ReadLaterView

urlpatterns = [path('', IndexView.as_view(), name='index_page'),
               path('about', AboutView.as_view(), name='about_page'),
               path('posts/<slug:post_slug>', UniquePostView.as_view(), name='post_page'),
               path('comment_submit', CommentSubmitView.as_view(), name='comment_submit'),
               path('read_later', ReadLaterView.as_view(), name='read_later'), ]
