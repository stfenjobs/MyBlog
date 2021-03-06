#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      filters.py 
@time:      2018/07/30 
"""

from blog.models import Post, Category, Tag, Resources
from blog import enums

from django_filters import rest_framework as filters
from dry_rest_permissions.generics import DRYPermissionFiltersBase


def get_author_posts(request):
    # 这里返回所有已经发表的博文，用于父级别过滤，不限于用户自身的
    return Post.objects.filter(
        status=enums.POST_STATUS_PUBLIC,
        post_type=enums.POST_TYPE_POST,
    )


class PostFilter(filters.FilterSet):
    parent = filters.ModelChoiceFilter(queryset=get_author_posts)

    class Meta:
        model = Post
        fields = {
            'parent': ['exact', 'isnull'],
            'author': ['exact'],
            'title': ['icontains'],
            'tags': ['icontains'],
            'category': ['exact'],
            'published_time': ['year__exact', 'month__exact']
        }


class ArchiveFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'published_time': ['year__exact', 'month__exact']
        }


class PostFilterBackend(DRYPermissionFiltersBase):
    """
    过滤博文列表
    """
    action_routing = True

    def filter_list_queryset(self, request, queryset, view):
        """
        返回所有用户已公开（发表）的博文，返回当前用户所有的博文（匿名用户只可查看公开博文）
        """
        query = {
            'status': enums.POST_STATUS_PUBLIC,
            'post_type': enums.POST_TYPE_POST
        }
        return queryset.filter(**query)

    def filter_get_notifications_queryset(self, request, queryset, view):
        """
        返回属于公告的博文
        """
        query = {
            'status': enums.POST_STATUS_PUBLIC,
            'post_type': enums.POST_TYPE_NOTIFICATION
        }
        return queryset.filter(**query)

    def filter_get_archives_queryset(self, request, queryset, view):
        """
        返回博文的归档列表
        """
        queryset = self.filter_list_queryset(request, queryset, view)
        return queryset.dates('published_time', 'month', order='DESC')

    def filter_get_hot_posts_queryset(self, request, queryset, view):
        """
        按浏览量返回热门博文
        """
        queryset = self.filter_list_queryset(request, queryset, view)
        return queryset.order_by('-n_browsers')

    def filter_get_max_praise_posts_queryset(self, request, queryset, view):
        queryset = self.filter_list_queryset(request, queryset, view)
        return queryset.order_by('-n_praise')

    def filter_get_banners_queryset(self, request, queryset, view):
        queryset = self.filter_list_queryset(request, queryset, view)
        query = {
            'is_banner': True
        }
        return queryset.filter(**query)


class CategoryFilterBackend(DRYPermissionFiltersBase):
    def filter_list_queryset(self, request, queryset, view):
        return queryset.filter(author=request.user)


def get_author_categories(request):
    """
    过滤器里只返回当前用户的分类
    :param request:
    :return:
    """
    if request.user.is_anonymous:
        return Category.objects.none()
    return Category.objects.filter(author=request.user)


class CategoryFilter(filters.FilterSet):
    parent = filters.ModelChoiceFilter(queryset=get_author_categories)

    class Meta:
        model = Category
        fields = {
            'parent': ['isnull', 'exact'],
            'name': ['icontains'],
        }


class TagFilterBackend(DRYPermissionFiltersBase):
    def filter_list_queryset(self, request, queryset, view):
        return queryset.filter(author=request.user)


class TagFilter(filters.FilterSet):
    class Meta:
        model = Tag
        fields = {
            "name": ['icontains'],
        }


class PostResourceBackend(DRYPermissionFiltersBase):
    def filter_list_queryset(self, request, queryset, view):
        return queryset.filter(post__author=request.user)


class PostResourceFilter(filters.FilterSet):
    class Meta:
        model = Resources
        fields = {
            "post": ['exact'],
            "name": ['icontains']
        }