#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/8/8.

from argeweb import BasicConfigModel
from argeweb import Fields
from datetime import datetime, timedelta


class ConfigModel(BasicConfigModel):
    class Meta:
        tab_pages = [u'設定']

    title = Fields.HiddenProperty(verbose_name=u'設定名稱', default=u'輪播圖設定')
    use_custom_name = Fields.BooleanProperty(verbose_name=u'自定義名稱', default=True)
    use_category = Fields.BooleanProperty(verbose_name=u'使用輪播圖分類', default=True)
    use_description = Fields.BooleanProperty(verbose_name=u'使用描述欄位', default=True)
    use_link = Fields.BooleanProperty(verbose_name=u'使用連結網址', default=True)
    use_background_image = Fields.BooleanProperty(verbose_name=u'使用背景底圖', default=False)

