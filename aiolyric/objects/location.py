"""Lyric location."""

from .base import LyricBaseClient, LyricBaseObject
from .device import LyricDevice


class LocationRoleMapping(LyricBaseObject):
    """Represents a location role mapping."""

    @property
    def location_id(self):
        """The ID of the location."""
        return self.attributes.get("locationID", None)

    @property
    def role(self):
        """The role of the location."""
        return self.attributes.get("role", None)

    @property
    def location_name(self):
        """The name of the location."""
        return self.attributes.get("locationName", None)

    @property
    def status(self):
        """The status of the location."""
        return self.attributes.get("status", None)


class User(LyricBaseObject):
    """Represents a user."""

    @property
    def user_id(self):
        """The ID of the user."""
        return self.attributes.get("userID", None)

    @property
    def username(self):
        """The username of the user."""
        return self.attributes.get("username", None)

    @property
    def first_name(self):
        """The first name of the user."""
        return self.attributes.get("firstname", None)

    @property
    def last_name(self):
        """The last name of the user."""
        return self.attributes.get("lastname", None)

    @property
    def created(self):
        """The creation date of the user."""
        return self.attributes.get("created", None)

    @property
    def deleted(self):
        """The deletion date of the user."""
        return self.attributes.get("deleted", None)

    @property
    def activated(self):
        """Whether the user is activated."""
        return self.attributes.get("activated", True)

    @property
    def connected_home_account_exists(self):
        """Whether a connected home account exists for the user."""
        return self.attributes.get("connectedHomeAccountExists", True)

    @property
    def location_role_mapping(self):
        """The location role mappings of the user."""
        return [
            LocationRoleMapping(x)
            for x in self.attributes.get("locationRoleMapping", [])
        ]

    @property
    def is_opt_out(self):
        """Whether the user has opted out."""
        return self.attributes.get("isOptOut", None)

    @property
    def is_current_user(self):
        """Whether the user is the current user."""
        return self.attributes.get("isCurrentUser", True)


class Time(LyricBaseObject):
    """Represents a time range."""

    @property
    def start(self):
        """The start time."""
        return self.attributes.get("start", None)

    @property
    def end(self):
        """The end time."""
        return self.attributes.get("end", None)


class Schedules(LyricBaseObject):
    """Represents a list of schedules."""

    @property
    def time(self):
        """The time ranges of the schedule."""
        return [Time(x) for x in self.attributes.get("time", [])]

    @property
    def days(self):
        """The days of the schedule."""
        return self.attributes.get("days", [])


class ConfigurationFaceRecognition(LyricBaseObject):
    """Represents the face recognition configuration."""

    @property
    def enabled(self):
        """Whether face recognition is enabled."""
        return self.attributes.get("enabled", False)

    @property
    def max_persons(self):
        """The maximum number of persons for face recognition."""
        return self.attributes.get("maxPersons", None)

    @property
    def max_etas(self):
        """The maximum number of ETAs for face recognition."""
        return self.attributes.get("maxEtas", None)

    @property
    def max_eta_persons(self):
        """The maximum number of ETA persons for face recognition."""
        return self.attributes.get("maxEtaPersons", None)

    @property
    def schedules(self):
        """The schedules for face recognition."""
        return [Schedules(x) for x in self.attributes.get("schedules", [])]


class Configuration(LyricBaseObject):
    """Represents the configuration of a location."""

    @property
    def face_recognition(self):
        """The face recognition configuration."""
        return ConfigurationFaceRecognition(self.attributes.get("faceRecognition", {}))


class LyricLocation(LyricBaseClient):
    """Represents a Lyric location."""

    @property
    def location_id(self):
        """The ID of the location."""
        return self.attributes.get("locationID", None)

    @property
    def name(self):
        """The name of the location."""
        return self.attributes.get("name", None)

    @property
    def country(self):
        """The country of the location."""
        return self.attributes.get("country", None)

    @property
    def zipcode(self):
        """The zipcode of the location."""
        return self.attributes.get("zipcode", None)

    @property
    def devices(self) -> list[LyricDevice]:
        """The devices associated with the location."""
        devices = []
        for x in self.attributes.get("devices", []):
            x["locationID"] = self.location_id
            devices.append(LyricDevice(self.client, x))
        return devices

    @property
    def devices_dict(self) -> dict:
        """A dictionary of devices associated with the location."""
        devices_dict: dict = {}
        for device in self.devices:
            devices_dict[device.mac_id] = device
        return devices_dict

    @property
    def users(self):
        """The users associated with the location."""
        return [User(x) for x in self.attributes.get("users", [])]

    @property
    def time_zone(self):
        """The timezone of the location."""
        return self.attributes.get("timeZone", None)

    @property
    def iana_time_zone(self):
        """The IANA timezone of the location."""
        return self.attributes.get("ianaTimeZone", None)

    @property
    def daylight_saving_time_enabled(self):
        """Whether daylight saving time is enabled for the location."""
        return self.attributes.get("daylightSavingTimeEnabled", True)

    @property
    def geo_fence_enabled(self):
        """Whether geofencing is enabled for the location."""
        return self.attributes.get("geoFenceEnabled", False)

    @property
    def predictive_air_enabled(self):
        """Whether predictive air is enabled for the location."""
        return self.attributes.get("predictiveAIREnabled", False)

    @property
    def comfort_level(self):
        """The comfort level of the location."""
        return self.attributes.get("comfortLevel", None)

    @property
    def geo_fence_notification_enabled(self):
        """Whether geofence notifications are enabled for the location."""
        return self.attributes.get("geoFenceNotificationEnabled", False)

    @property
    def geo_fence_notification_type_id(self):
        """The ID of the geofence notification type for the location."""
        return self.attributes.get("geoFenceNotificationTypeId", None)

    @property
    def configuration(self):
        """The configuration of the location."""
        return Configuration(self.attributes.get("configuration", {}))
