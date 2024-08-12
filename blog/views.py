from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Author, Post, Tag, Comment
from django.views import View
from django.views.generic.base import TemplateView
from .forms import CommentForm
from datetime import date


def get_date(post):
    return post['date']


class IndexView(View):
    template_name = 'blog/index.html'

    def get(self, request):
        posts = Post.objects.all().order_by('-date')
        read_later_list = []
        if request.session.get('read_later_list'):
            read_later_list = request.session.get('read_later_list')
        return render(request, self.template_name, {'posts': posts, 'read_later_list': read_later_list})


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class ContactView(TemplateView):
    template_name = 'blog/contact.html'


class UniquePostView(View):
    template_name = 'blog/post.html'
    comment_form = CommentForm

    def get(self, request, *args, **kwargs):
        post_slug = self.kwargs['post_slug']
        post = Post.objects.get(slug=post_slug)
        comments = Comment.objects.filter(post=post).order_by('-date')
        read_later_ids = []
        if request.session.get('read_later_list'):
            read_later_ids = request.session.get('read_later_list')
        print('Read later ids: ', read_later_ids)
        in_read_later_list = False
        print(post.id)
        if post.id in read_later_ids:
            in_read_later_list = True

        return render(request, self.template_name, context={
            'post': post,
            'form': self.comment_form(),
            'comments': comments,
            'in_read_later_list': in_read_later_list
        })


class CommentSubmitView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post_slug = request.POST.get('post_slug')
        post_id = request.POST.get('post_id')
        print(post_slug)
        redirection = reverse('post_page', args=[post_slug])
        if form.is_valid():
            print('checked')
            post = Post.objects.get(id=post_id)
            comment = Comment(
                username=form.cleaned_data['username'],
                comment=form.cleaned_data['comment'],
                post=post
            )
            comment.save()
            print(form.cleaned_data['username'])
        return HttpResponseRedirect(redirection)


class ReadLaterView(View):
    def post(self, request, *args, **kwargs):
        if request.POST.get('remove_read_later_post_id'):
            read_later_ids = request.session.get('read_later_list')
            post_id_to_be_removed = int(request.POST.get('remove_read_later_post_id'))
            read_later_ids.remove(post_id_to_be_removed)
            request.session['read_later_list'] = read_later_ids
        else:
            if request.session.get('read_later_list'):
                read_later_ids = request.session.get('read_later_list')
                read_later_ids.append(int(request.POST.get('read_later_post_id')))
                read_later_ids = list(dict.fromkeys(read_later_ids))
                request.session['read_later_list'] = read_later_ids
            else:
                read_later_ids = [int(request.POST.get('read_later_post_id'))]
                read_later_ids = list(dict.fromkeys(read_later_ids))
                request.session['read_later_list'] = read_later_ids
        slug = request.POST.get('post_slug')
        redirection = reverse('post_page', args=[slug])
        print('Redirection is ', redirection)
        return HttpResponseRedirect(redirection)
