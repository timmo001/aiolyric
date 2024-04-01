"""Lyric device."""

from .base import LyricBaseClient, LyricBaseObject


class Vacationhold(LyricBaseObject):
    """Vacation hold."""

    @property
    def enabled(self):
        """Return if enabled."""
        return self.attributes.get("enabled", False)


class Currentscheduleperiod(LyricBaseObject):
    """Current schedule period."""

    @property
    def day(self):
        """Return the day."""
        return self.attributes.get("day", None)

    @property
    def period(self):
        """Return the period."""
        return self.attributes.get("period", None)


class Schedulecapabilities(LyricBaseObject):
    """Schedule capabilities."""

    @property
    def availableScheduleTypes(self):
        """Return available schedule types."""
        return self.attributes.get("availableScheduleTypes", [])

    @property
    def schedulableFan(self):
        """Return if fan is schedulable."""
        return self.attributes.get("schedulableFan", False)


class Scheduletype(LyricBaseObject):
    """Schedule type."""

    @property
    def scheduleType(self):
        """Return the schedule type."""
        return self.attributes.get("scheduleType", None)

    @property
    def scheduleSubType(self):
        """Return the schedule sub type."""
        return self.attributes.get("scheduleSubType", None)


class SettingsHardwaresettings(LyricBaseObject):
    """Hardware settings."""

    @property
    def brightness(self):
        """Return the brightness."""
        return self.attributes.get("brightness", None)

    @property
    def maxBrightness(self):
        """Return the max brightness."""
        return self.attributes.get("maxBrightness", None)


class SettingsTemperaturemode(LyricBaseObject):
    """Temperature mode."""

    @property
    def air(self):
        """Return if air is enabled."""
        return self.attributes.get("air", True)


class SettingsSpecialmode(LyricBaseObject):
    """Special mode."""

    @property
    def _(self):
        """Return None."""
        return None


class SettingsFan(LyricBaseObject):
    """Fan settings."""

    @property
    def fan(self):
        """Return the fan settings."""
        return self.attributes.get("fan", {})


class Settings(LyricBaseObject):
    """Settings."""

    @property
    def hardwareSettings(self):
        """Return hardware settings."""
        return SettingsHardwaresettings(self.attributes.get("hardwareSettings", {}))

    @property
    def temperatureMode(self):
        """Return temperature mode."""
        return SettingsTemperaturemode(self.attributes.get("temperatureMode", {}))

    @property
    def specialMode(self):
        """Return special mode."""
        return SettingsSpecialmode(self.attributes.get("specialMode", {}))

    @property
    def devicePairingEnabled(self):
        """Return if device pairing is enabled."""
        return self.attributes.get("devicePairingEnabled", True)

    @property
    def fanModes(self):
        """Return fan modes."""
        return SettingsFan(self.attributes.get("allowedModes", []))

    @property
    def fanChangeableValues(self):
        """Return fan changeable values."""
        return SettingsFan(self.attributes.get("changeableValues", {}))

    @property
    def fanMode(self):
        """Return the fan mode."""
        return SettingsFan(self.attributes.get("mode", None))


class Devicesettings(LyricBaseObject):
    """Device settings."""

    @property
    def _(self):
        """Return None."""
        return None


class Service(LyricBaseObject):
    """Service."""

    @property
    def mode(self):
        """Return the mode."""
        return self.attributes.get("mode", None)


class Changeablevalues(LyricBaseObject):
    """Changeable values."""

    @property
    def autoChangeoverActive(self):
        """Return if auto changeover is active."""
        return self.attributes.get("autoChangeoverActive", None)

    @property
    def mode(self):
        """Return the mode."""
        return self.attributes.get("mode", None)

    @property
    def heatSetpoint(self):
        """Return the heat setpoint."""
        return self.attributes.get("heatSetpoint", None)

    @property
    def coolSetpoint(self):
        """Return the cool setpoint."""
        return self.attributes.get("coolSetpoint", None)

    @property
    def thermostatSetpointStatus(self):
        """Return the thermostat setpoint status."""
        return self.attributes.get("thermostatSetpointStatus", None)

    @property
    def nextPeriodTime(self):
        """Return the next period time."""
        return self.attributes.get("nextPeriodTime", None)

    @property
    def heatCoolMode(self):
        """Return the heat cool mode."""
        return self.attributes.get("heatCoolMode", None)

    @property
    def endHeatSetpoint(self):
        """Return the end heat setpoint."""
        return self.attributes.get("endHeatSetpoint", None)

    @property
    def endCoolSetpoint(self):
        """Return the end cool setpoint."""
        return self.attributes.get("endCoolSetpoint", None)


class Operationstatus(LyricBaseObject):
    """Operation status."""

    @property
    def mode(self):
        """Return the mode."""
        return self.attributes.get("mode", None)

    @property
    def fanRequest(self):
        """Return the fan request."""
        return self.attributes.get("fanRequest", False)

    @property
    def circulationFanRequest(self):
        """Return the circulation fan request."""
        return self.attributes.get("circulationFanRequest", False)


class LyricDevice(LyricBaseClient):
    """Lyric Device."""

    @property
    def locationID(self):
        """Return the location ID."""
        return self.attributes.get("locationID", None)

    @property
    def indoorHumidity(self):
        """Return the indoor humidity."""
        return self.attributes.get("indoorHumidity", None)

    @property
    def displayedOutdoorHumidity(self):
        """Return the displayed outdoor humidity."""
        return self.attributes.get("displayedOutdoorHumidity", None)

    @property
    def vacationHold(self):
        """Return the vacation hold."""
        return Vacationhold(self.attributes.get("vacationHold", {}))

    @property
    def currentSchedulePeriod(self):
        """Return the current schedule period."""
        return Currentscheduleperiod(self.attributes.get("currentSchedulePeriod", {}))

    @property
    def scheduleCapabilities(self):
        """Return the schedule capabilities."""
        return Schedulecapabilities(self.attributes.get("scheduleCapabilities", {}))

    @property
    def scheduleType(self):
        """Return the schedule type."""
        return Scheduletype(self.attributes.get("scheduleType", {}))

    @property
    def scheduleStatus(self):
        """Return the schedule status."""
        return self.attributes.get("scheduleStatus", None)

    @property
    def allowedTimeIncrements(self):
        """Return the allowed time increments."""
        return self.attributes.get("allowedTimeIncrements", None)

    @property
    def settings(self):
        """Return the settings."""
        return Settings(self.attributes.get("settings", {}))

    @property
    def deviceClass(self):
        """Return the device class."""
        return self.attributes.get("deviceClass", None)

    @property
    def deviceType(self):
        """Return the device type."""
        return self.attributes.get("deviceType", None)

    @property
    def deviceID(self):
        """Return the device ID."""
        return self.attributes.get("deviceID", None)

    @property
    def name(self):
        """Return the name."""
        return self.attributes.get("name", None)

    @property
    def isAlive(self):
        """Return if the device is alive."""
        return self.attributes.get("isAlive", True)

    @property
    def isUpgrading(self):
        """Return if the device is upgrading."""
        return self.attributes.get("isUpgrading", False)

    @property
    def isProvisioned(self):
        """Return if the device is provisioned."""
        return self.attributes.get("isProvisioned", True)

    @property
    def macID(self):
        """Return the MAC ID."""
        return self.attributes.get("macID", None)

    @property
    def deviceSettings(self):
        """Return the device settings."""
        return Devicesettings(self.attributes.get("deviceSettings", {}))

    @property
    def service(self):
        """Return the service."""
        return Service(self.attributes.get("service", {}))

    @property
    def deviceRegistrationDate(self):
        """Return the device registration date."""
        return self.attributes.get("deviceRegistrationDate", None)

    @property
    def dataSyncStatus(self):
        """Return the data sync status."""
        return self.attributes.get("dataSyncStatus", None)

    @property
    def units(self):
        """Return the units."""
        return self.attributes.get("units", None)

    @property
    def indoorTemperature(self):
        """Return the indoor temperature."""
        return self.attributes.get("indoorTemperature", None)

    @property
    def outdoorTemperature(self):
        """Return the outdoor temperature."""
        return self.attributes.get("outdoorTemperature", None)

    @property
    def allowedModes(self):
        """Return the allowed modes."""
        return self.attributes.get("allowedModes", [])

    @property
    def deadband(self):
        """Return the deadband."""
        return self.attributes.get("deadband", None)

    @property
    def hasDualSetpointStatus(self):
        """Return if the device has dual setpoint status."""
        return self.attributes.get("hasDualSetpointStatus", False)

    @property
    def minHeatSetpoint(self):
        """Return the minimum heat setpoint."""
        return self.attributes.get("minHeatSetpoint", None)

    @property
    def maxHeatSetpoint(self):
        """Return the maximum heat setpoint."""
        return self.attributes.get("maxHeatSetpoint", None)

    @property
    def minCoolSetpoint(self):
        """Return the minimum cool setpoint."""
        return self.attributes.get("minCoolSetpoint", None)

    @property
    def maxCoolSetpoint(self):
        """Return the maximum cool setpoint."""
        return self.attributes.get("maxCoolSetpoint", None)

    @property
    def changeableValues(self):
        """Return the changeable values."""
        return Changeablevalues(self.attributes.get("changeableValues", {}))

    @property
    def operationStatus(self):
        """Return the operation status."""
        return Operationstatus(self.attributes.get("operationStatus", {}))

    @property
    def deviceModel(self):
        """Return the device model."""
        return self.attributes.get("deviceModel", None)
