#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields
from banner_category_model import BannerCategoryModel


class BannerModel(BasicModel):
    title = Fields.StringProperty(verbose_name=u'標題')
    link = Fields.StringProperty(verbose_name=u'連結網址')
    description = Fields.TextProperty(verbose_name=u'描述')
    image = Fields.ImageProperty(verbose_name=u'圖片')
    background_image = Fields.ImageProperty(verbose_name=u'背景底圖')
    is_enable = Fields.BooleanProperty(verbose_name=u'啟用', default=True)
    category = Fields.CategoryProperty(verbose_name=u'分類', kind=BannerCategoryModel)
    category_name = Fields.SearchingHelperProperty(verbose_name=u'所屬產品', target='category', target_field_name='name')

    @classmethod
    def all_enable(cls, category=None, *args, **kwargs):
        return cls.query(cls.category_name==category, cls.is_enable==True).order(-cls.sort)
