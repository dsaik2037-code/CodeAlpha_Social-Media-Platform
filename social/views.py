from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Profile



def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/home.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(user=user)

        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'social/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'social/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user_posts = Post.objects.filter(
        user=request.user
    ).order_by('-created_at')

    followers = request.user.followers.all()
    following = request.user.following.all()

    users = User.objects.exclude(id=request.user.id)

    return render(
        request,
        'social/profile.html',
        {
            'user_posts': user_posts,
            'followers': followers,
            'following': following,
            'users': users,
        }
    )


def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        content = request.POST['content']
        image = request.FILES.get('image')

        Post.objects.create(
            user=request.user,
            content=content,
            image=image
        )

        return redirect('home')

    return render(request, 'social/create_post.html')
def like_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')

    post = Post.objects.get(id=post_id)

    from .models import Like

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect('home')


def add_comment(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')

    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        from .models import Comment

        content = request.POST['content']

        if content.strip():
            Comment.objects.create(
                post=post,
                user=request.user,
                content=content
            )

    return redirect('home')
def follow_user(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')

    user_to_follow = User.objects.get(id=user_id)

    if request.user == user_to_follow:
        return redirect('profile')

    from .models import Follow

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )

    if not created:
        follow.delete()

    return redirect('profile')
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Only the person who created the post can delete it
    if post.user != request.user:
        return redirect('home')

    if request.method == 'POST':
        post.delete()

    return redirect('home')