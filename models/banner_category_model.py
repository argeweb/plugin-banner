#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields


class BannerCategoryModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(verbose_name=u'分類標題')
    is_enable = Fields.BooleanProperty(verbose_name=u'啟用', default=True)

    @classmethod
    def all_enable(cls):
        return cls.query(cls.is_enable==True).order(-cls.sort)

    @classmethod
    def insert(cls, name, title, is_enable=True):
        item = cls.find_by_name(name)
        if item is not None:
            return
        item = cls()
        item.name = name
        item.title = title
        item.is_enable = is_enable
        item.put()
        return item
