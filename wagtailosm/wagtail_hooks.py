from osm_field.widgets import _get_css, _get_js

from django.conf import settings
from django.utils.html import format_html_join

# Wagtail 1 or Wagtail 2?
try:
    from wagtail.wagtailcore import hooks
except ImportError:
    from wagtail.core import hooks


@hooks.register('insert_editor_js')
def editor_js():
    """
    Add extra JS files to the admin
    """
    js_files = _get_js(settings.DEBUG)
    js_includes = format_html_join(
        '\n',
        '<script type="text/javascript" src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )

    return js_includes


@hooks.register('insert_editor_css')
def editor_css():
    """
    Add extra JS files to the admin
    """
    css_files = _get_css(settings.DEBUG) + ['wagtailosm/css/wagtailadmin.css']
    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}{1}">',
        ((settings.STATIC_URL, filename) for filename in css_files)
    )

    return css_includes
