#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2016/07/08.

from argeweb import ViewDatastore
from models.banner_model import BannerModel
from models.banner_model import BannerCategoryModel

ViewDatastore.register('banner_list', BannerModel.all_enable)

plugins_helper = {
    'title': u'輪播圖',
    'desc': u'具分類的輪播圖',
    'controllers': {
        'banner': {
            'group': u'輪播圖',
            'actions': [
                {'action': 'list', 'name': u'輪播圖管理'},
                {'action': 'add', 'name': u'新增輪播圖'},
                {'action': 'edit', 'name': u'編輯輪播圖'},
                {'action': 'view', 'name': u'檢視輪播圖'},
                {'action': 'delete', 'name': u'刪除輪播圖'},
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        },
        'banner_category': {
            'group': u'輪播圖分類',
            'actions': [
                {'action': 'list', 'name': u'輪播圖分類管理'},
                {'action': 'add', 'name': u'新增輪播圖分類'},
                {'action': 'edit', 'name': u'編輯輪播圖分類'},
                {'action': 'view', 'name': u'檢視輪播圖分類'},
                {'action': 'delete', 'name': u'刪除輪播圖分類'},
            ]
        }
    }
}