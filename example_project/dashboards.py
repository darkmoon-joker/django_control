from controlcenter import Dashboard, widgets

from example_project import simple_widgets
from example_project import widgets as _widgets


class ExampleDashboard(Dashboard):
    widgets = [
        _widgets.MenuWidget,
        _widgets.LatestOrdersWidget,
        _widgets.RestaurantSingleBarChart,
    ]


class SimpleWidgetsDashboard(Dashboard):
    widgets = [
        simple_widgets.AppInfoWidget,
        simple_widgets.DebuggingEndpointsWidget,
    ]
