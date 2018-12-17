from django.shortcuts import render, redirect
from .models import Hero, Video, Comment
from django.contrib.auth import get_user_model
from . import form
from django.template.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponse

User = get_user_model()

def index(request):
    content = []
    for her in Hero.objects.all():
        content.append(her)
    return render(
        request,
        'index.html',
        context={'content': content}
        )

def show(request, hero_id):
    her = Hero.objects.get(id=hero_id)
    vids = []
    for vid in Video.objects.all():
        if her.Hero_name in vid.Video_name:
            vids.append(vid)
    return render(
        request,
        'highlights.html',
        context={'her': her, 'vids': vids}
        )

def ShowOne(request, video_id):
    video = Video.objects.get(id=video_id)
    args = {}
    args.update(csrf(request))
    args['form'] = form.CommentForm
    args['video'] = video
    args['user'] = auth.get_user(request).username
    comments = Comment.objects.filter(Comment_Video_id=video_id)
    Users_list = []
    for com in comments:
        Users_list.append(User.objects.get(id=com.Comment_User_id))
    args['comments'] = list(zip(comments, Users_list))
    for her in Hero.objects.all():
        if her.Hero_name in video.Video_name:
            hero = her
    args['hero'] = hero

    return render(
        request,
        'onevideo.html',
        context=args
        )

def addcomment(request, video_id):
    if request.POST:
        forma = form.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit = False)
            comment.Comment_Video = Video.objects.get(id=video_id)
            comment.Comment_User = User.objects.get(id=request.user.id)
            forma.save()
    return redirect("/main/showOne/" + str(video_id) + "/")

def sign(request):
    if request.POST:
        user = User.objects.create_user(username=request.POST.get('username', ""),
                                        email=request.POST.get('email', ""),
                                        password=request.POST.get('password', ""))
        if user.is_authenticated:
            auth.login(request, user)
        return redirect('/main/')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = form.UserForm
        args['url'] = "/main/sign/"
        args['user'] = auth.get_user(request).username
        return render(request, 'sign.html', args)

def out(request):
    auth.logout(request)
    return redirect('/main/')

def inn(request):
    if request.POST:
        user = auth.authenticate(username=request.POST.get('username', ""),
                                 password=request.POST.get('password', ""))
        if user.is_authenticated:
            auth.login(request, user)
            return redirect('/main/')
        else:
            args = {}
            args.update(csrf(request))
            args['user'] = auth.get_user(request).username
            args['form'] = form.UserFormL
            args['url'] = '/main/in/'
            args["error"] = "Такой пользователь не найден"
            return render(request, 'sign.html', args)
    else:
        args = {}
        args.update(csrf(request))
        args['user'] = auth.get_user(request).username
        args['form'] = form.UserFormL
        args['url'] = '/main/in/'
        return render(request, 'sign.html', args)

def addliketovideo(request, video_id):
    video = Video.objects.get(id=video_id)
    video.Video_likes += 1
    video.save()
    return redirect('/main/showOne/' + str(video_id))

def addliketocomment(request, comment_id):
    comment = Comment.objects.get(id = comment_id)
    comment.Comment_likes += 1
    comment.save()
    idvideo = comment.Comment_Video_id
    return redirect('/main/showOne/' + str(idvideo))
