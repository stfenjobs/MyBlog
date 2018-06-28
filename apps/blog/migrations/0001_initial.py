# Generated by Django 2.0.3 on 2018-06-28 18:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类目名称')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.Category')),
            ],
            options={
                'verbose_name': '博文类目',
                'verbose_name_plural': '博文类目',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='少于50字符', max_length=50, verbose_name='博文标题')),
                ('cover', models.ImageField(default='blog/blog_cover/default.jpg', max_length=200, upload_to='blog/blog_cover/%Y/%m', verbose_name='博文封面')),
                ('cover_url', models.URLField(default='', verbose_name='博文封面url')),
                ('excerpt', models.TextField(blank=True, verbose_name='博文摘要')),
                ('content', models.TextField(verbose_name='博文内容')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('published', '已发表')], default='draft', max_length=10, verbose_name='编辑状态')),
                ('n_praise', models.PositiveIntegerField(default=0, verbose_name='点赞数量')),
                ('n_browsers', models.PositiveIntegerField(default=0, verbose_name='浏览次数')),
                ('published_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')),
                ('type', models.CharField(choices=[('post', '博文'), ('notification', '公告')], default='post', max_length=13, verbose_name='博文类型')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否是轮播图')),
                ('origin_post_url', models.URLField(default='', verbose_name='原博文URL链接')),
                ('origin_post_from', models.CharField(default='', max_length=255, verbose_name='原博文出处名称')),
                ('url_object_id', models.CharField(max_length=255, unique=True, verbose_name='源博文唯一标识')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='博文作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='博文类目')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.Post', verbose_name='上一篇博文')),
            ],
            options={
                'verbose_name': '博文',
                'verbose_name_plural': '博文',
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='资源名称')),
                ('resource', models.FileField(max_length=200, upload_to='blog/resources/%Y/%m/', verbose_name='资源文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='blog.Post', verbose_name='所属博文')),
            ],
            options={
                'verbose_name': '博文资源',
                'verbose_name_plural': '博文资源',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '博文标签',
                'verbose_name_plural': '博文标签',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='博文标签'),
        ),
    ]
