# Datetime_sensors

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE.md)

this is a **homeassistant** custom-component to make create a `binary-sensor` for any `input_datetime`. With this componente, the `binary_sensor` follows the `input_datetime` value to get `on` state when the time as the `input_datetime` are matched. otherwise it returns `off` state. Very useful to use this with a `automation` trigger.

## Why?

Currently, to use any `input_datetime` as a trigger, we need create a `trigger-template` whit a non easy reminder logic. For this reason, I made this simple component (*under-construction*) to make this action more easy. Whit this component, you only need create a `binary_sensor` with this platform and a sensor will be created to follow the `input_datetime` value.

## Installation

At the moment, this component is * under-construction *. For this reason, It doesn't be finded in HACS repository. However, you can install it alike using HACS adding this github repo in your ** Hacs Settings ** temporarily.

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[license-shield]: https://img.shields.io/github/license/skal88/custom-components-datetime-sensors.svg?style=for-the-badge
[commits]: https://github.com/skal88/custom-components-datetime-sensors/commits/master
[commits-shield]: https://img.shields.io/github/commit-activity/y/skal88/custom-components-datetime-sensors.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/v/release/skal88/custom-components-datetime-sensors.svg?style=for-the-badge
[releases]: https://github.com/skal88/custom-components-datetime-sensors/releases