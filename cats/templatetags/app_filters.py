from django.template.defaultfilters import register


@register.filter
def return_item_by_index(l, i):
    try:
        return l[i-1]
    except IndexError:
        return None
