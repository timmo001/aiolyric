"""Lyric group."""

from .base import LyricBaseObject


class LyricGroupAccessoryAttribute(LyricBaseObject):
    """Details of an accessory in a group room."""

    @property
    def type(self):
        """Get the type of the accessory."""
        return self.attributes.get("type", None)

    @property
    def connection_method(self):
        """Get how the accessory connects to the thermostat."""
        return self.attributes.get("connectionMethod", None)

    @property
    def name(self):
        """Get the name of the accessory."""
        return self.attributes.get("name", None)

    @property
    def model(self):
        """Get the model of the accessory."""
        return self.attributes.get("model", None)

    @property
    def serial_number(self):
        """Get the serial number of the accessory."""
        return self.attributes.get("serialNumber", None)

    @property
    def software_revision(self):
        """Get the software revision of the accessory."""
        return self.attributes.get("softwareRevision", None)

    @property
    def hardware_revision(self):
        """Get the hardware revision of the accessory."""
        return self.attributes.get("hardwareRevision", None)


class LyricGroupAccessoryValue(LyricBaseObject):
    """Readings of an accessory in a group room."""

    @property
    def cool_setpoint(self):
        """Get the cool setpoint of the accessory."""
        return self.attributes.get("coolSetpoint", None)

    @property
    def heat_setpoint(self):
        """Get the heat setpoint of the accessory."""
        return self.attributes.get("heatSetpoint", None)

    @property
    def indoor_humidity(self):
        """Get the humidity at the accessory."""
        return self.attributes.get("indoorHumidity", None)

    @property
    def indoor_temperature(self):
        """Get the temperature at the accessory."""
        return self.attributes.get("indoorTemperature", None)

    @property
    def motion_detected(self):
        """Check if motion is detected."""
        return self.attributes.get("motionDet", False)

    @property
    def occupancy_detected(self):
        """Check if the room is occupied."""
        return self.attributes.get("occupancyDet", False)

    @property
    def exclude_temp(self):
        """Check if temperature is excluded from operation."""
        return self.attributes.get("excludeTemp", False)

    @property
    def exclude_motion(self):
        """Check if motion is excluded from operation."""
        return self.attributes.get("excludeMotion", False)

    @property
    def pressure(self):
        """Get the pressure at the accessory."""
        return self.attributes.get("pressure", None)

    @property
    def occupancy_sensitivity(self):
        """Get the sensitivity of the occupancy sensor."""
        return self.attributes.get("occupancySensitivity", None)

    @property
    def occupancy_timeout(self):
        """Get the occupancy timeout."""
        return self.attributes.get("occupancyTimeout", None)

    @property
    def status(self):
        """Get the status of the accessory."""
        return self.attributes.get("status", None)

    @property
    def battery_status(self):
        """Get the battery status of the accessory."""
        return self.attributes.get("batteryStatus", None)

    @property
    def rssi_average(self):
        """Get the signal strength to the thermostat."""
        return self.attributes.get("rssiAverage", None)


class LyricGroupAccessory(LyricBaseObject):
    """Accessory in a group room."""

    @property
    def id(self):
        """Get the ID of the accessory."""
        return self.attributes.get("accessoryId", None)

    @property
    def attribute(self):
        """Get the details of the accessory."""
        return LyricGroupAccessoryAttribute(
            self.attributes.get("accessoryAttribute", {})
        )

    @property
    def value(self):
        """Get the readings of the accessory."""
        return LyricGroupAccessoryValue(self.attributes.get("accessoryValue", {}))


class LyricGroupRoom(LyricBaseObject):
    """Room in a group."""

    @property
    def id(self):
        """Get the ID of the room."""
        return self.attributes.get("id", None)

    @property
    def name(self):
        """Get the name of the room."""
        return self.attributes.get("name", None)

    @property
    def type(self):
        """Get the type of the room."""
        return self.attributes.get("type", None)

    @property
    def avg_temperature(self):
        """Get the average temperature of the room."""
        return self.attributes.get("avgTemperature", None)

    @property
    def avg_humidity(self):
        """Get the average humidity of the room."""
        return self.attributes.get("avgHumidity", None)

    @property
    def accessories(self):
        """Get the accessories in the room."""
        return [LyricGroupAccessory(x) for x in self.attributes.get("accessories", [])]


class LyricGroup(LyricBaseObject):
    """Rooms in a group on a thermostat."""

    @property
    def device_id(self):
        """Get the ID of the thermostat."""
        return self.attributes.get("deviceId", None)

    @property
    def group_id(self):
        """Get the ID of the group."""
        return self.attributes.get("groupId", None)

    @property
    def rooms(self):
        """Get the rooms in the group."""
        return [LyricGroupRoom(x) for x in self.attributes.get("rooms", [])]
