from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm
from microblog.models import Profile, Post

@login_required
def index(request):
	profile = Profile.objects.get(user__username=request.user)
	latestPosts = Post.objects.filter(profile__in=profile.following.all()).order_by('-pub_date')[:15]
	context = {
		'latestPosts': latestPosts,
		'profile': profile,
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


