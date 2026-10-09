"""Lyric priority."""

from .base import LyricBaseObject


def _first(attributes: dict, *keys: str, default=None):
    """Return the first present key.

    Resideo serves two schemas for the priority endpoint depending on the
    account, so every field is read from both the current and the classic
    key (see https://github.com/timmo001/aiolyric/pull/165).
    """
    for key in keys:
        if key in attributes:
            return attributes[key]
    return default


class LyricAccessory(LyricBaseObject):
    """Lyric accessory."""

    @property
    def id(self):
        """Get the ID of the accessory."""
        return self.attributes.get("id", None)

    @property
    def type(self):
        """Get the type of the accessory."""
        return _first(self.attributes, "sensorType", "type", default="")

    @property
    def exclude_temp(self):
        """Check if temperature is excluded for the accessory."""
        return _first(
            self.attributes, "excludeTemperature", "excludeTemp", default=False
        )

    @property
    def exclude_motion(self):
        """Check if motion is excluded for the accessory."""
        return self.attributes.get("excludeMotion", False)

    @property
    def temperature(self):
        """Get the temperature of the accessory."""
        return self.attributes.get("temperature", None)

    @property
    def status(self):
        """Get the status of the accessory."""
        return self.attributes.get("status", "")

    @property
    def detect_motion(self):
        """Check if motion is detected for the accessory."""
        return self.attributes.get("detectMotion", False)


class LyricRoom(LyricBaseObject):
    """Class representing Lyric rooms."""

    @property
    def id(self):
        """Get the ID of the room."""
        return self.attributes.get("id", None)

    @property
    def room_name(self):
        """Get the name of the room."""
        return _first(self.attributes, "name", "roomName", default="")

    @property
    def room_avg_temp(self):
        """Get the average temperature of the room."""
        return _first(self.attributes, "avgTemperature", "roomAvgTemp")

    @property
    def room_avg_humidity(self):
        """Get the average humidity of the room."""
        return _first(self.attributes, "avgHumidity", "roomAvgHumidity")

    @property
    def overall_motion(self):
        """Check if motion is detected in the room."""
        return self.attributes.get("overallMotion", False)

    @property
    def accessories(self):
        """Get the list of accessories in the room."""
        return [LyricAccessory(x) for x in self.attributes.get("accessories", [])]


class CurrentPriority(LyricBaseObject):
    """Class representing the current priority."""

    @property
    def priority_type(self):
        """Get the type of the priority."""
        return self.attributes.get("priorityType", "")

    @property
    def selected_rooms(self):
        """Get the list of selected rooms for the priority."""
        return self.attributes.get("selectedRooms", [])

    @property
    def rooms(self):
        """Get the list of rooms for the priority."""
        return [LyricRoom(x) for x in self.attributes.get("rooms", [])]


class LyricPriority(LyricBaseObject):
    """Class representing Lyric priority."""

    @property
    def device_id(self):
        """Get the ID of the device."""
        return self.attributes.get("deviceId", "")

    @property
    def status(self):
        """Get the status of the priority."""
        return _first(self.attributes, "priorityStatus", "status", default="")

    @property
    def current_priority(self):
        """Get the current priority."""
        return CurrentPriority(
            _first(self.attributes, "priority", "currentPriority", default={})
        )
