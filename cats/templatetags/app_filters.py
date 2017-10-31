from django.template.defaultfilters import register


@register.filter
def return_item_by_index(l, i):
    try:
        return l[i-1]
    except IndexError:
        return None


@register.filter
def change_page(query, page=None):
    """

    :type query: QueryDict
    """
    query._mutable = True
    if page is not None:
        query['page'] = page
    try:
        res = query.urlencode()
    except AttributeError:
        res = ''
    return res
