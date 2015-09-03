from django.contrib.sitemaps import Sitemap
from datetime import datetime
from django.core.urlresolvers import reverse

class MemberSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

class test(Sitemap):
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names
    def changefreq(self, obj):
        return 'weekly'
    def lastmod(self, obj):
        return datetime.now()
    def location(self, obj):
        return reverse(obj)