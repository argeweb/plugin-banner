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
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    description = Fields.TextProperty(verbose_name=u'描述')
    link = Fields.StringProperty(verbose_name=u'連結網址')
    link_title = Fields.StringProperty(verbose_name=u'連結標題')
    image = Fields.ImageProperty(verbose_name=u'圖片')
    is_enable = Fields.BooleanProperty(verbose_name=u'啟用', default=True)
    category = Fields.CategoryProperty(verbose_name=u'分類', kind=BannerCategoryModel)

    @classmethod
    def all_enable(cls, category=None, *args, **kwargs):
        cat = None
        if category:
            cat = BannerCategoryModel.find_by_name(category)
        if cat is None:
            return cls.query(cls.is_enable==True).order(-cls.sort)
        else:
            return cls.query(cls.category==cat.key, cls.is_enable==True).order(-cls.sort)
