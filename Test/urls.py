"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from blog.views import index,view_post,view_category
from pkg_resources import parse_version
from django.views.generic import TemplateView
from chartnew import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', 'blog.views.index'),
    url(r'^blog/','blog.views.view_post', name='view_blog_post'),
    url(r'^category/', 'blog.views.view_category', name='view_blog_category'),

    url(r'^colors/$', views.colors, name='colors'),

    # Column
    url(r'^column_highchart/json/$', views.column_highchart_json,
        name='column_highchart_json'),

    # Line chart
    url(r'^line_chart/$', views.line_chart,
        name='line_chart'),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json'),
    url(r'^line_highchart/json/$', views.line_highchart_json,
        name='line_highchart_json'),

    # Pie
    url(r'^pie_highchart/json/$', views.pie_highchart_json,
        name='pie_highchart_json'),
    url(r'^donut_highchart/json/$', views.donut_highchart_json,
        name='donut_highchart_json'),
]


