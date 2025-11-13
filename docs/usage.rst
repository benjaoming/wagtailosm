========
Usage
========

Add ``wagtailosm`` and ``osm_field`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'osm_field',
        'wagtailosm',
        # ...
    )

The order does not matter, but we need both of these applications to be registered because they contain static files.

Example 1
---------

In this example, we use default values for latitude and longitude.
This means the map has a default location when displayed for the first time.
The latitude and longitude fields are HIDDEN, so the user has a simple interface
where they just need to choose a location on the map.

.. code-block:: python

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

        # Add to Wagtail admin's panels - example with hidden lat/lon fields
        content_panels = Page.content_panels + [
            FieldPanel('location', widget=osm_field.fields.OSMWidget('latitude', 'longitude'), classname="wagtailosm-location"),
            FieldPanel('latitude', classname="wagtailosm-hidden"),
            FieldPanel('longitude', classname="wagtailosm-hidden"),
        ]

Example 2
---------

In this example, there is no default value, and we expect the default use-case to be that the user provides the latitude and longitude value.

They use the map in case they do not have these values and need an alternative to choosing them since every interaction with the map causes the lat/lon to be overwritten!

.. code-block:: python

    class Country(Page):

        location = OSMField(blank=True, lat_field="latitude", lon_field="longitude")
        latitude = LatitudeField(default=None, null=True)
        longitude = LongitudeField(default=None, null=True)

        # This is handled by the map, but don't forget you will probably need
        # to be able to customize this...
        zoom_level = models.PositiveSmallIntegerField(default=15)

        # Add to Wagtail admin's panels - example with hidden lat/lon fields
        content_panels = Page.content_panels + [
            FieldPanel(
                "latitude",
            ),
            FieldPanel(
                "longitude",
            ),
            FieldPanel(
                "location",
                widget=OSMWidget("latitude", "longitude"),
                classname="wagtailosm-location",
                help_text=_("Choose location on map (instead of typing coordinates)"),
            ),
        ]
