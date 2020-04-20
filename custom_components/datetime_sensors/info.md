[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]

**This component will set up the following platforms.**
Platform | Description
-- | --
`binary_sensor` | Show something `on` or `off`.

{% if not installed %}
## Installation

1. Click install.
1. Add follow example:

{% endif %}
## Example configuration.yaml

```yaml
binary_sensor:
  - platform: datetime_sensors
    datetime_input: input_datetime.my_input_datetime
    name: my_datetime_is_triggered
```

## Configuration options

Key | Type | Required | Description
-- | -- | -- | --
`datetime_input` | `entity_id` | `True` | entity as `input_datetime` type you like track
`name` | `string` | `False` | Custom name for this `binary_sensor`

***

[license-shield]: https://img.shields.io/github/license/skal88/custom-components-datetime-sensors.svg?style=for-the-badge
[commits]: https://github.com/skal88/custom-components-datetime-sensors/commits/master
[commits-shield]: https://img.shields.io/github/commit-activity/y/skal88/custom-components-datetime-sensors.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/v/release/skal88/custom-components-datetime-sensors.svg?style=for-the-badge
[releases]: https://github.com/skal88/custom-components-datetime-sensors/releases