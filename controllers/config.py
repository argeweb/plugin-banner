#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/8/8.

from argeweb import Controller, scaffold, route_menu, route


class Config(Controller):
    class Scaffold:
        display_in_list = ['is_enable', 'category']
        hidden_in_form = ['name', 'title', 'use']

    @staticmethod
    def change_config(controller, item, *args, **kwargs):
        if item.use_category is True:
            controller.fire('enable_role_action', action_uri='plugins.banner.controllers.banner_category.list')
        else:
            controller.fire('disable_role_action', action_uri='plugins.banner.controllers.banner_category.list')

    @route
    @route_menu(list_name=u'super_user', text=u'輪播圖', sort=3930, group=u'內容管理', need_hr=True)
    def admin_config(self):
        config_record = self.meta.Model.get_config()
        self.events.scaffold_after_save += self.change_config
        return scaffold.edit(self, config_record.key)
