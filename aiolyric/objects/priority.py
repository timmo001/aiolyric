"""Lyric priority."""

from .base import LyricBaseObject


class LyricAccessories(LyricBaseObject):
    """Lyric accessories."""

    @property
    def id(self):
        """Get the ID of the accessory."""
        return self.attributes.get("id", None)

    @property
    def type(self):
        """Get the type of the accessory."""
        return self.attributes.get("type", "")

    @property
    def excludeTemp(self):
        """Check if temperature is excluded for the accessory."""
        return self.attributes.get("excludeTemp", False)

    @property
    def excludeMotion(self):
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
    def detectMotion(self):
        """Check if motion is detected for the accessory."""
        return self.attributes.get("detectMotion", False)


class LyricRoom(LyricBaseObject):
    """Class representing Lyric rooms."""

    @property
    def id(self):
        """Get the ID of the room."""
        return self.attributes.get("id", None)

    @property
    def roomName(self):
        """Get the name of the room."""
        return self.attributes.get("roomName", "")

    @property
    def roomAvgTemp(self):
        """Get the average temperature of the room."""
        return self.attributes.get("roomAvgTemp", None)

    @property
    def roomAvgHumidity(self):
        """Get the average humidity of the room."""
        return self.attributes.get("roomAvgHumidity", None)

    @property
    def overallMotion(self):
        """Check if motion is detected in the room."""
        return self.attributes.get("overallMotion", False)

    @property
    def accessories(self):
        """Get the list of accessories in the room."""
        return [LyricAccessories(x) for x in self.attributes.get("accessories", [])]


class CurrentPriority(LyricBaseObject):
    """Class representing the current priority."""

    @property
    def priorityType(self):
        """Get the type of the priority."""
        return self.attributes.get("priorityType", "")

    @property
    def selectedRooms(self):
        """Get the list of selected rooms for the priority."""
        return self.attributes.get("selectedRooms", [])

    @property
    def rooms(self):
        """Get the list of rooms for the priority."""
        return [LyricRoom(x) for x in self.attributes.get("rooms", [])]


class LyricPriority(LyricBaseObject):
    """Class representing Lyric priority."""

    @property
    def deviceId(self):
        """Get the ID of the device."""
        return self.attributes.get("deviceId", "")

    @property
    def status(self):
        """Get the status of the priority."""
        return self.attributes.get("status", "")

    @property
    def currentPriority(self):
        """Get the current priority."""
        return CurrentPriority(self.attributes.get("currentPriority", {}))
