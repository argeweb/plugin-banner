#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu, Fields, route_with
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search


class Banner(Controller):
    class Scaffold:
        display_in_list = ('name', 'image', 'is_enable', 'category')

    @route_menu(list_name=u'backend', text=u'輪播圖', sort=316, group=u'內容管理')
    def admin_list(self):
        return scaffold.list(self)
