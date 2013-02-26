
/*
 Read only Google Maps in the client area.

 How it works:

 Enter a coordinates, map scale and canvas id.
 A marker will be placed at the address.

 Only one marker will remain present on the map at a time.

 This script expects:

 <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

 */

function googleMapClient() {

    var map;
    var marker;

    var self = {
        initialize: function(lat, lng, zoom, canvas) {
            var latlng = new google.maps.LatLng(lat,lng);
            var myOptions = {
                zoom: zoom,
                center: latlng,
                mapTypeId: google.maps.MapTypeId.HYBRID
            };
            map = new google.maps.Map(document.getElementById(canvas), myOptions);
            self.addMarker({'latlng': latlng, 'draggable': false});
        },

        addMarker: function(Options) {
            marker = new google.maps.Marker({
                map: map,
                position: Options.latlng
            });
        }
    };

    return self;
}
