from django.shortcuts import render
from django .contrib.sitemaps import Sitemap
from member.models import UserProfile

# Create your views here.
def LoginView(request):
    a = 123
    return render(request, 'member/login.html')


