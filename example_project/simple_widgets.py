from controlcenter.widgets.contrib import simple as widgets
from controlcenter.utils import DataItem
from django.conf import settings


class DebuggingEndpointsWidget(widgets.ValueList):
    title = 'Debugging Endpoints'

    subtitle = 'Links for debugging application issues'

    def get_data(self):
        return [
            # Plain text displays as a row in the widget.
            'Not really sure why you would want plain text here',
            # Dictionary defining a display label and a url.
            {'label': 'Datadog Dashboard', 'url': 'https://example.com'},
            # `DataItem` can be used as an alternative to dictionaries.
            DataItem(label='Healthcheck', url='https://example.com',
                     help_text='Healthcheck report for external dependencies'),
        ]


class AppInfoWidget(widgets.KeyValueList):
    title = 'App info'

    def get_data(self):
        return {
            # A simple key-value pair
            'Language code': settings.LANGUAGE_CODE,
            # A dictionary value can be used to display a link
            'Default timezone': {
                'label': settings.TIME_ZONE,
                'url': 'https://docs.djangoproject.com/en/2.1/topics/i18n/timezones/',
            },
            # To display a key with a link, you must use `DataItem` instead
            # of a dictionary, since keys must be hashable.
            DataItem(
                label='Debug on',
                url='https://docs.djangoproject.com/en/2.1/ref/settings/#debug'
            ): settings.DEBUG,
        }
