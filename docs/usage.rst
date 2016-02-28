========
Usage
========

Add ``wagtailosm`` and ``osm_field`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...
        'osm_field',
        'wagtailosm',
        # ...
    )

The order does not matter, but we need both of these applications to be registered because they contain static files.

To have a field with a map displayed in Wagtail, do this::


    class Country(Page):

        # If you are adding this field to an existing model, you need to define some
        # default location for populating existing rows in the migration.
        DEFAULT_LAT, DEFAULT_LON = (52.4864, 13.4385)

        location = OSMField(default=(DEFAULT_LAT, DEFAULT_LON), lat_field='latitude', lon_field='longitude')
        latitude = LatitudeField(default=DEFAULT_LAT)
        longitude = LongitudeField(default=DEFAULT_LON)

        # This is handled by the map, but don't forget you will probably need
        # to be able to customize this...
        zoom_level = models.PositiveSmallIntegerField(default=15)

        # Add to Wagtail admin's panels
        content_panels = Page.content_panels + [
            FieldPanel('location', widget=osm_field.fields.OSMWidget('latitude', 'longitude'), classname="wagtailosm-location"),
            FieldPanel('latitude', classname="wagtailosm-hidden"),
            FieldPanel('longitude', classname="wagtailosm-hidden"),
        ]

