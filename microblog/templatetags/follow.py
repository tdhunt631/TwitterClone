from django import template
from microblog.models import Profile
from django.shortcuts import render, get_object_or_404

register = template.Library()

@register.inclusion_tag('microblog/follow.html', takes_context = True)
def listProfiles(context):
	profileList = Profile.objects.all()
	profiles = []
	for profile in profileList:
		profiles.append(profile)
	return {'profiles': profiles}
