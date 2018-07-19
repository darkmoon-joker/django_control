"""
Generic widgets for `django-controlcenter` dashboards that don't require model data.
"""
from __future__ import (absolute_import, division, print_function, unicode_literals)

from . import core


__all__ = ['SimpleWidget', 'ValueList', 'KeyValueList']


class SimpleWidget(core.BaseWidget):

    width = core.MEDIUM
    template_name_prefix = 'controlcenter/widgets'

    def get_data(self):
        raise NotImplementedError("SimpleWidget subclass must implement `get_data`")


class ValueList(SimpleWidget):

    template_name = 'value_list.html'
    value_column_label = None
    sortable = False

    def show_column_headers(self):
        return self.sortable or self.value_column_label

    def items(self):
        return self.get_data()


class KeyValueList(SimpleWidget):

    template_name = 'key_value_list.html'
    key_column_label = None
    value_column_label = None
    sortable = False

    def show_column_headers(self):
        return self.sortable or self.key_column_label or self.value_column_label

    def items(self):
        return self.get_data().items()
