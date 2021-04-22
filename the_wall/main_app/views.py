from django.shortcuts import render, redirect
from user_control.models import User
from .models import Thread, Comment


def index(request):
    if 'uuid' not in request.session:
        return redirect("/")
    context = {
        'user': User.objects.get(id = request.session['uuid']),
        'board_threads': Thread.objects.all()}
    return render(request, 'main_app/index.html', context)


def make_thread(request):
    Thread.objects.create(
        user=User.objects.get(id = request.session['uuid']),
        content=request.POST['thread_post_box'])
    return redirect('/thewall')


def make_comment(request):
    Comment.objects.create(
        user=User.objects.get(id=request.session['uuid']),
        thread=Thread.objects.get(id=request.POST['thread_id']),
        content=request.POST['comment_post_box'])
    return redirect('/thewall')


def delete_comment(request, comment_id):
    comment_to_delete= Comment.objects.get(id=comment_id)
    comment_to_delete.delete()
    return redirect('/thewall')


def delete_thread(request, thread_id):
    thread_to_delete= Thread.objects.get(id=thread_id)
    thread_to_delete.delete()
    return redirect('/thewall')