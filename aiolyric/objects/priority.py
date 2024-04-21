"""Lyric priority."""

from .base import LyricBaseObject


class LyricAccessory(LyricBaseObject):
    """Lyric accessory."""

    @property
    def id(self):
        """Get the ID of the accessory."""
        return self.attributes.get("id", None)

    @property
    def type(self):
        """Get the type of the accessory."""
        return self.attributes.get("type", "")

    @property
    def exclude_temp(self):
        """Check if temperature is excluded for the accessory."""
        return self.attributes.get("excludeTemp", False)

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
        return self.attributes.get("roomName", "")

    @property
    def room_avg_temp(self):
        """Get the average temperature of the room."""
        return self.attributes.get("roomAvgTemp", None)

    @property
    def room_avg_humidity(self):
        """Get the average humidity of the room."""
        return self.attributes.get("roomAvgHumidity", None)

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
        return self.attributes.get("status", "")

    @property
    def current_priority(self):
        """Get the current priority."""
        return CurrentPriority(self.attributes.get("currentPriority", {}))
