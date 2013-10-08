from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm
from microblog.models import Profile, Post, PostForm
from django.template import RequestContext

@login_required
def index(request):
	profile = Profile.objects.get(user__username=request.user)
	latestPosts = Post.objects.filter(profile__in=profile.following.all()).order_by('-pub_date')[:15]
	postForm = PostForm()
	context = {
		'latestPosts': latestPosts,
		'profile': profile,
		'postForm': postForm,
}
	return render(request, 'microblog/index.html', context)


@login_required
def profile(request):
	myProfile = get_object_or_404(Profile, user=request.user)
	following = myProfile.following	
	context = {
		'myProfile': myProfile,
		'following': following,
	}
	return render(request, 'microblog/profile.html', context)

@login_required
def detail(request, user):
	latestPosts = Post.objects.all().filter(profile=user)
	profile = get_object_or_404(Profile, user=user)
	context = {
		'profile': profile,
		'latestPosts': latestPosts,
	}
	return render(request, 'microblog/detail.html', context)

@login_required
def addPost(request, profile_id):
	if request.method == 'POST':
		data = PostForm(request.POST)
		form = data.save(commit=False)
		form.profile = get_object_or_404(Profile, id=profile_id)
		form.save()
		if request.is_ajax():
			profile = get_object_or_404(Profile, id=profile_id) 
			latestPosts = Post.objects.filter(profile__in=profile.following.all()).order_by('-pub_date')[:15]
			context = {
				'profile': profile,
				'latestPosts': latestPosts,
			}		
			return render_to_response('microblog/newPost.html', context, context_instance=RequestContext(request))
	return HttpResponseRedirect('/')
