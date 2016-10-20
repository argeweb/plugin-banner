#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import BasicModel
from argeweb import Fields


class BannerCategoryModel(BasicModel):
    class Meta:
        label_name = {
            "name": u"識別名稱",
            "title": u"分類標題",
            "is_enable": u"啟用",
        }
    name = Fields.StringProperty()
    title = Fields.StringProperty()
    is_enable = Fields.BooleanProperty(default=True)

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
