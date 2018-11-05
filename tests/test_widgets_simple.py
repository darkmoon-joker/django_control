from controlcenter.widgets.contrib import simple

from . import TestCase


FAKE_VALUE_LIST = ['Label 1', 'Label 2']
FAKE_KEY_VALUE_LIST = {'Key 1': 'Value 1', 'Key 2': 'Value 2'}


class ValueListTest(TestCase):

    def setUp(self):
        self.widget = ExampleValueList(request=None)

    def test_basic(self):
        self.assertIsNotNone(self.widget.template_name)

    def test_default_not_sortable(self):
        self.assertFalse(self.widget.sortable)

    def test_get_data(self):
        self.assertItemsEqual(self.widget.items(), FAKE_VALUE_LIST)


class KeyValueListTest(TestCase):

    def setUp(self):
        self.widget = ExampleKeyValueList(request=None)

    def test_basic(self):
        self.assertIsNotNone(self.widget.template_name)

    def test_default_not_sortable(self):
        self.assertFalse(self.widget.sortable)

    def test_get_data(self):
        self.assertItemsEqual(self.widget.items(), FAKE_KEY_VALUE_LIST.items())


class ExampleValueList(simple.ValueList):
    title = 'Value list widget'

    def get_data(self):
        return FAKE_VALUE_LIST


class ExampleKeyValueList(simple.KeyValueList):
    title = 'Key-value list widget'

    def get_data(self):
        return FAKE_KEY_VALUE_LIST
