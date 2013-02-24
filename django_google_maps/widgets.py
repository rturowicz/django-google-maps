
from django.forms import widgets
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt

from .settings import GOOGLE_MAPS_CSS_URL, GOOGLE_MAPS_JS_URL, GOOGLE_MAPS_JQUERY_URL


class GoogleMapsAddressWidget(widgets.TextInput):
    "a widget that will place a google map right after the #id_address field"
    
    class Media:
        css = {'all': (GOOGLE_MAPS_CSS_URL + '/google-maps-admin.css',),}
        js = (
            GOOGLE_MAPS_JQUERY_URL + '/jquery.min.js',
            'http://maps.google.com/maps/api/js?sensor=false',
            GOOGLE_MAPS_JS_URL + '/google-maps-admin.js',
        )

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(u'<input%s /><div class="map_canvas_wrapper"><div id="map_canvas"></div></div>' % flatatt(final_attrs))
