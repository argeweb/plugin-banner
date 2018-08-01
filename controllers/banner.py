#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2015/7/12.

from argeweb import Controller, scaffold, route_menu
from ..models.config_model import ConfigModel


class Banner(Controller):
    class Scaffold:
        display_in_list = ['title', 'link', 'image', 'is_enable', 'category']

    @route_menu(list_name=u'backend', group=u'內容管理', text=u'輪播圖', sort=316)
    def admin_list(self):
        return scaffold.list(self)

    def admin_add(self):
        return scaffold.add(self)

    def admin_edit(self, key):
        return scaffold.edit(self, key)

    def before_scaffold(self):
        super(Banner, self).before_scaffold()
        config = ConfigModel.get_or_create_by_name('banner_config')
        self.scaffold.change_field_visibility('name', config.use_custom_name, config.use_custom_name)
        self.scaffold.change_field_visibility('category', config.use_category, config.use_category)
        self.scaffold.change_field_visibility('link', config.use_description, config.use_description)
        self.scaffold.change_field_visibility('description', config.use_link, config.use_link)
        self.scaffold.change_field_visibility('background_image', config.use_background_image, config.use_background_image)
