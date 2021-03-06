#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu


class BannerCategory(Controller):
    class Scaffold:
        display_in_list = ['name', 'title', 'is_enable']

    @route_menu(list_name=u'backend', group=u'內容管理', text=u'輪播圖分類', sort=317)
    def admin_list(self):
        return scaffold.list(self)
