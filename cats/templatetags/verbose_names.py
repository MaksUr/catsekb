from django import template

register = template.Library()


@register.simple_tag
def get_verbose_field_name(instance, field_name):
    """

    :type field_name: str
    :type instance: django.db.models.Model
    """
    return instance._meta.get_field(field_name).verbose_name.title()


@register.simple_tag
def get_default_value_for_form(field_name, counter, query_dict, choice):
    if query_dict.get(field_name) == choice:
        return " checked='checked'"
    elif query_dict.get(field_name) is not None:
        return ''
    elif int(counter) == 0:
        return " checked='checked'"
    else:
        return ''


@register.simple_tag
def return_page_by_object(objects, obj, per_page):
    if per_page:
        index = ((list(objects).index(obj)) / per_page) + 1
        return int(index)
    else:
        return 100




