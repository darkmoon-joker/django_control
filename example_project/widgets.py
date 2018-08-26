from django.db.models import Count
from django.utils import timezone
from django.utils.timesince import timesince
from controlcenter import app_settings, widgets
from .models import Order, Pizza, Restaurant


class MenuWidget(widgets.ItemList):
    """Scrollable `ItemList` widget with fixed height."""

    title = "Ciao's pizzas"
    model = Restaurant
    list_display = ['name', 'ocount']
    list_display_links = ['name']

    # By default ItemList limits queryset to 10 items, but we need all of them
    limit_to = None

    # Sets widget's max-height to 300 px and makes it scrollable
    height = 300

    def get_queryset(self):
        restaurant = super(MenuWidget, self).get_queryset().get(name='Ciao')
        today = timezone.now().date()
        return (restaurant.menu
                .filter(orders__created__gte=today)
                .order_by('-ocount')
                .annotate(ocount=Count('orders')))


class LatestOrdersWidget(widgets.ItemList):
    """Sortable and enumerated `ItemList`."""

    title = 'Latest orders'
    model = Order
    queryset = (
        model.objects
        .select_related('pizza')
        .filter(created__gte=timezone.now().date())
        .order_by('pk')
    )
    # Add `SHARP` sign to make `ItemList` ennumerate rows.
    list_display = [app_settings.SHARP, 'pk', 'pizza', 'ago']

    # If list_display_links is not defined, first column to be linked
    list_display_links = ['pk']

    # Makes list sortable
    sortable = True

    # Shows last 20
    limit_to = 20

    # Display time since instead of date.__str__
    def ago(self, obj):
        return timesince(obj.created)


class RestaurantSingleBarChart(widgets.SingleBarChart):
    # Displays score of each restaurant.
    title = 'Most popular restaurant'
    model = Restaurant

    class Chartist:
        options = {
            # Displays only integer values on y-axis
            'onlyInteger': True,
            # Visual tuning
            'chartPadding': {
                'top': 24,
                'right': 0,
                'bottom': 0,
                'left': 0,
            }
        }

    def legend(self):
        # Duplicates series in legend, because Chartist.js
        # doesn't display values on bars
        return self.series

    def values(self):
        # Returns pairs of restaurant names and order count.
        queryset = self.get_queryset()
        return (
            queryset
            .values_list('name')
            .annotate(baked=Count('orders'))
            .order_by('-baked')[:self.limit_to]
        )
