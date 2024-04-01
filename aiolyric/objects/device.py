"""Lyric device."""

from .base import LyricBaseClient, LyricBaseObject


class VacationHold(LyricBaseObject):
    """Vacation hold."""

    @property
    def enabled(self):
        """Return if enabled."""
        return self.attributes.get("enabled", False)


class CurrentSchedulePeriod(LyricBaseObject):
    """Current schedule period."""

    @property
    def day(self):
        """Return the day."""
        return self.attributes.get("day", None)

    @property
    def period(self):
        """Return the period."""
        return self.attributes.get("period", None)


class ScheduleCapabilities(LyricBaseObject):
    """Schedule capabilities."""

    @property
    def available_schedule_types(self):
        """Return available schedule types."""
        return self.attributes.get("availableScheduleTypes", [])

    @property
    def schedulable_fan(self):
        """Return if fan is schedulable."""
        return self.attributes.get("schedulableFan", False)


class ScheduleType(LyricBaseObject):
    """Schedule type."""

    @property
    def schedule_type(self):
        """Return the schedule type."""
        return self.attributes.get("scheduleType", None)

    @property
    def schedule_sub_type(self):
        """Return the schedule sub type."""
        return self.attributes.get("scheduleSubType", None)


class SettingsHardwareSettings(LyricBaseObject):
    """Hardware settings."""

    @property
    def brightness(self):
        """Return the brightness."""
        return self.attributes.get("brightness", None)

    @property
    def max_brightness(self):
        """Return the max brightness."""
        return self.attributes.get("maxBrightness", None)


class SettingsTemperatureMode(LyricBaseObject):
    """Temperature mode."""

    @property
    def air(self):
        """Return if air is enabled."""
        return self.attributes.get("air", True)


class SettingsSpecialMode(LyricBaseObject):
    """Special mode."""


class Settings(LyricBaseObject):
    """Settings."""

    @property
    def hardware_settings(self):
        """Return hardware settings."""
        return SettingsHardwareSettings(self.attributes.get("hardwareSettings", {}))

    @property
    def temperature_mode(self):
        """Return temperature mode."""
        return SettingsTemperatureMode(self.attributes.get("temperatureMode", {}))

    @property
    def special_mode(self):
        """Return special mode."""
        return SettingsSpecialMode(self.attributes.get("specialMode", {}))

    @property
    def device_pairing_enabled(self):
        """Return if device pairing is enabled."""
        return self.attributes.get("devicePairingEnabled", True)


class DeviceSettings(LyricBaseObject):
    """Device settings."""


class Service(LyricBaseObject):
    """Service."""

    @property
    def mode(self):
        """Return the mode."""
        return self.attributes.get("mode", None)


class ChangeableValues(LyricBaseObject):
    """Changeable values."""

    @property
    def mode(self):
        """Return the mode."""
        return self.attributes.get("mode", None)

    @property
    def auto_changeover_active(self):
        """Return if auto changeover is active."""
        return self.attributes.get("autoChangeoverActive", None)

    @property
    def emergency_heat_active(self):
        """Return the thermostat setpoint status."""
        return self.attributes.get("emergencyHeatActive", None)

    @property
    def heat_setpoint(self):
        """Return the heat setpoint."""
        return self.attributes.get("heatSetpoint", None)

    @property
    def cool_setpoint(self):
        """Return the cool setpoint."""
        return self.attributes.get("coolSetpoint", None)

    @property
    def thermostat_setpoint_status(self):
        """Return the thermostat setpoint status."""
        return self.attributes.get("thermostatSetpointStatus", None)

    @property
    def next_period_time(self):
        """Return the next period time."""
        return self.attributes.get("nextPeriodTime", None)

    @property
    def heat_cool_mode(self):
        """Return the heat cool mode."""
        return self.attributes.get("heatCoolMode", None)

    @property
    def end_heat_setpoint(self):
        """Return the end heat setpoint."""
        return self.attributes.get("endHeatSetpoint", None)

    @property
    def end_cool_setpoint(self):
        """Return the end cool setpoint."""
        return self.attributes.get("endCoolSetpoint", None)


class OperationStatus(LyricBaseObject):
    """Operation status."""

    @property
    def mode(self):
        """Return the mode."""
        return self.attributes.get("mode", None)

    @property
    def fan_request(self):
        """Return the fan request."""
        return self.attributes.get("fanRequest", False)

    @property
    def circulation_fan_request(self):
        """Return the circulation fan request."""
        return self.attributes.get("circulationFanRequest", False)


class LyricDevice(LyricBaseClient):
    """Lyric Device."""

    @property
    def location_id(self):
        """Return the location ID."""
        return self.attributes.get("locationID", None)

    @property
    def indoor_humidity(self):
        """Return the indoor humidity."""
        return self.attributes.get("indoorHumidity", None)

    @property
    def displayed_outdoor_humidity(self):
        """Return the displayed outdoor humidity."""
        return self.attributes.get("displayedOutdoorHumidity", None)

    @property
    def vacation_hold(self):
        """Return the vacation hold."""
        return VacationHold(self.attributes.get("vacationHold", {}))

    @property
    def current_schedule_period(self):
        """Return the current schedule period."""
        return CurrentSchedulePeriod(self.attributes.get("currentSchedulePeriod", {}))

    @property
    def schedule_capabilities(self):
        """Return the schedule capabilities."""
        return ScheduleCapabilities(self.attributes.get("scheduleCapabilities", {}))

    @property
    def schedule_type(self):
        """Return the schedule type."""
        return ScheduleType(self.attributes.get("scheduleType", {}))

    @property
    def schedule_status(self):
        """Return the schedule status."""
        return self.attributes.get("scheduleStatus", None)

    @property
    def allowed_time_increments(self):
        """Return the allowed time increments."""
        return self.attributes.get("allowedTimeIncrements", None)

    @property
    def settings(self):
        """Return the settings."""
        return Settings(self.attributes.get("settings", {}))

    @property
    def device_class(self):
        """Return the device class."""
        return self.attributes.get("deviceClass", None)

    @property
    def device_type(self):
        """Return the device type."""
        return self.attributes.get("deviceType", None)

    @property
    def device_id(self):
        """Return the device ID."""
        return self.attributes.get("deviceID", None)

    @property
    def name(self):
        """Return the name."""
        return self.attributes.get("name", None)

    @property
    def is_alive(self):
        """Return if the device is alive."""
        return self.attributes.get("isAlive", True)

    @property
    def is_upgrading(self):
        """Return if the device is upgrading."""
        return self.attributes.get("isUpgrading", False)

    @property
    def is_provisioned(self):
        """Return if the device is provisioned."""
        return self.attributes.get("isProvisioned", True)

    @property
    def mac_id(self):
        """Return the MAC ID."""
        return self.attributes.get("macID", None)

    @property
    def device_settings(self):
        """Return the device settings."""
        return DeviceSettings(self.attributes.get("deviceSettings", {}))

    @property
    def service(self):
        """Return the service."""
        return Service(self.attributes.get("service", {}))

    @property
    def device_registration_date(self):
        """Return the device registration date."""
        return self.attributes.get("deviceRegistrationDate", None)

    @property
    def data_sync_status(self):
        """Return the data sync status."""
        return self.attributes.get("dataSyncStatus", None)

    @property
    def units(self):
        """Return the units."""
        return self.attributes.get("units", None)

    @property
    def indoor_temperature(self):
        """Return the indoor temperature."""
        return self.attributes.get("indoorTemperature", None)

    @property
    def outdoor_temperature(self):
        """Return the outdoor temperature."""
        return self.attributes.get("outdoorTemperature", None)

    @property
    def allowed_modes(self):
        """Return the allowed modes."""
        return self.attributes.get("allowedModes", [])

    @property
    def deadband(self):
        """Return the deadband."""
        return self.attributes.get("deadband", None)

    @property
    def has_dual_setpoint_status(self):
        """Return if the device has dual setpoint status."""
        return self.attributes.get("hasDualSetpointStatus", False)

    @property
    def min_heat_setpoint(self):
        """Return the minimum heat setpoint."""
        return self.attributes.get("minHeatSetpoint", None)

    @property
    def max_heat_setpoint(self):
        """Return the maximum heat setpoint."""
        return self.attributes.get("maxHeatSetpoint", None)

    @property
    def min_cool_setpoint(self):
        """Return the minimum cool setpoint."""
        return self.attributes.get("minCoolSetpoint", None)

    @property
    def max_cool_setpoint(self):
        """Return the maximum cool setpoint."""
        return self.attributes.get("maxCoolSetpoint", None)

    @property
    def changeable_values(self):
        """Return the changeable values."""
        return ChangeableValues(self.attributes.get("changeableValues", {}))

    @property
    def operation_status(self):
        """Return the operation status."""
        return OperationStatus(self.attributes.get("operationStatus", {}))

    @property
    def device_model(self):
        """Return the device model."""
        return self.attributes.get("deviceModel", None)

    @property
    def fan_mode(self):
        """Return the fan mode."""
        return self.attributes.get("fanMode", None)
