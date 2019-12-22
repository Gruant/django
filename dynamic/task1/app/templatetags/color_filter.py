from django import template

register = template.Library()


@register.filter
def color_filter(value):
    try:
        item = float(value)
        if item < 0:
            return "green"
        else:
            if 1.0 < item < 3.0:
                return "#FA8072"
            elif 3.0 < item < 5.0:
                return "#ED2949"
            elif item > 5.0:
                return "red"
            else:
                return "white"
    except ValueError:
        return value
