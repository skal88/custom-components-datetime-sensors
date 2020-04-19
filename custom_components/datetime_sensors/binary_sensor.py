"""Binary sensor platform for blueprint."""

import logging

import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.binary_sensor import (
    BinarySensorDevice,
    PLATFORM_SCHEMA,
    DOMAIN,
    STATE_OFF,
    STATE_ON,
)
from homeassistant.util import dt
from homeassistant.const import (
    CONF_NAME,
    CONF_ENTITY_ID,
    CONF_FRIENDLY_NAME,
    CONF_TIME_ZONE,
    EVENT_STATE_CHANGED,
    EVENT_TIME_CHANGED,
    STATE_UNKNOWN,
)
from .const import (
    BINARY_SENSOR_DEVICE_CLASS,
    DEFAULT_SENSOR_NAME_SUFFIX,
    DOMAIN_DATA,
)
import datetime
from pytz import timezone

CONF_DATETIME_INPUT = "datetime_input"

ATTR_DATETIME_INPUT = "input_datetime_entity"

# Validations
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_DATETIME_INPUT): cv.entity_id,
        vol.Optional(CONF_NAME): cv.string,
        vol.Optional(CONF_FRIENDLY_NAME): cv.string,
    }
)


def setup_platform(
    hass, config, add_entities, discovery_info=None
):  # pylint: disable=unused-argument
    """Setup binary_sensor platform."""

    add_entities([MyCustomBinarySensor(hass, config,)])


class MyCustomBinarySensor(BinarySensorDevice):
    def __init__(self, hass, config):
        self.hass = hass
        self.attr = {
            CONF_FRIENDLY_NAME: config.get(CONF_NAME),
            ATTR_DATETIME_INPUT: config.get(CONF_DATETIME_INPUT),
        }
        self._status = STATE_OFF
        self._name = config.get(CONF_NAME)

        if not config.get(CONF_NAME):
            self._name = config.get(CONF_DATETIME_INPUT) + DEFAULT_SENSOR_NAME_SUFFIX

        hass.bus.listen(EVENT_STATE_CHANGED, self.state_changed)
        hass.bus.listen(EVENT_TIME_CHANGED, self.time_changed)

    def state_changed(self, event):
        if not event.data[CONF_ENTITY_ID] == self.attr[ATTR_DATETIME_INPUT]:
            return

        self.update()

    def time_changed(self, time):
        self.update()

    def update(self):
        input_datetime = self.hass.states.get(self.attr[ATTR_DATETIME_INPUT])
        if not input_datetime:
            return STATE_UNKNOWN

        now = dt.as_local(datetime.datetime.now())
        now_time = datetime.datetime(
            1970, 1, 1, int(now.strftime("%H")), int(now.strftime("%M"))
        )

        input_time = datetime.datetime(
            1970,
            1,
            1,
            input_datetime.attributes["hour"],
            input_datetime.attributes["minute"],
        )

        #  Refactor - Use homeassistant utils:
        # https://dev-docs.home-assistant.io/en/master/api/util.html#module-homeassistant.util.dt

        last_state = self._status

        if datetime.datetime.timestamp(now_time) == datetime.datetime.timestamp(
            input_time
        ):
            self._status = STATE_ON
        else:
            self._status = STATE_OFF

        if last_state != self._status:
            self.hass.states.set(DOMAIN + "." + self._name, self._status, self.attr)

        return self._status

    @property
    def unique_id(self):
        """Return a unique ID to use for this binary_sensor."""
        return (
            self.attr[ATTR_DATETIME_INPUT] + " " + self._name
        )  # Don't hard code this, use something from the device/service.

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": self.name,
            "manufacturer": "Blueprint",
        }

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return self._name

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self._status

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.attr
