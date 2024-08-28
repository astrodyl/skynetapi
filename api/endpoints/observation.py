from typing import Optional, List

from api.endpoints.endpoint import Endpoint
from api.endpoints.exposure import Exposure
from api.endpoints.trigger import Trigger


"""
    Observation Class
    
    The Observation class mimics the Skynet observation schema. Attributes
    are explicitly defined, rather than generically like in the Exposures
    class, to better help the user understand what can be done with the
    Observation class.
    
    Methods are provided to convert the class to and from a dictionary. This
    is useful when interacting with the API as it returns a dictionary with
    camel case keys. It can be convenient to use a class object with snake
    case when working in Python instead.
    
    Attributes that are 'required' are only required for sending a POST request
    to the 'obs' endpoint of the Skynet API. I protected attributes that a user
    should never have a purpose of modifying. These attributes are only set 
    internally when the data is received from the Skynet API.
"""


class Observation(Endpoint):
    def __init__(self, **kw):
        super().__init__()

        # [Protected] Set upon API query
        self._id: int | None = None
        self._type: str | None = None
        self._state: str | None = None
        self._time_submitted_utc: str | None = None

        # [Required] Observation Parameters
        self.name: str | None = None                                # Name of the observation
        self.mode: int | None = None                                # One of 0, 1, 2
        self.time_account_id: int | None = None                     # Time account to credit credits

        # [Required] Telescope Parameters
        self.telescopes: List[str | int] = []                       # Telescopes to observe with

        # [Optional] Object Parameters
        self.object_name: Optional[str] = None                      # Name of the object
        self.object_type: Optional[str] = None                      # Type of the object
        self.object_dist: Optional[float] = None                    # Distance to solar system object in AU

        # [Required] Coordinates
        self.ra_hours: float | None = None                          # Right Ascension of the object (between 0 and 24)
        self.dec_degs: float | None = None                          # Declination of the object (between -90 and 90)

        # [Required] Observing Constraints
        self.min_el: float | None = None                            # Maximum allowed sun elevation in degrees (<= -6)
        self.max_sun: float | None = None                           # Minimum allowed object elevation in degrees
        self.min_moon_sep_degs: float | None = None                 # Minimum allowed separation from the moon

        # [Required] Tracking Parameters
        self.target_tracking: str | None = None                     # One of track_target or lock_field
        self.field_lock_utc: str | None = None                      # Lock field at the given UTC

        # [Required] Exposure Parameters
        self.exps: list = []                                        # Exposure requests

        # [Optional] Exposure Parameters
        self.cancel_after_utc: Optional[str] = None                 # Cancel observation after this time
        self.next_exp_start_after_utc: Optional[str] = None         # Delay start of observation until this time

        # [Optional] Observation Parameters
        self.efficiency: Optional[float] = None                     # Assumes exposure lengths

        # [Optional] Priority Parameters
        self.priority: Optional[int] = None                         # Priority of the observation
        self.is_too: Optional[bool] = None                          # Target-Of-Opportunity (TOO)
        self.too_justification: Optional[str] = None                # Justification for using TOO

        # [Optional] Pointing Parameters
        self.point_ahead_enabled: Optional[bool] = None
        self.point_ahead_secs: Optional[int] = None
        self.constant_ra_offset_arcmins: Optional[float] = None
        self.constant_dec_offset_arcmins: Optional[float] = None

        self.trigger_repoint_enabled: Optional[bool] = None
        self.trigger_repoint_arcmins: Optional[float] = None
        self.rbi_fraction_avg_bkg_limit: Optional[float] = None

        # [Optional] Dithering Parameters
        self.dither_enabled: Optional[bool] = None
        self.ditherX_size: Optional[float] = None
        self.ditherY_size: Optional[float] = None
        self.dither_spacing_arcsecs: Optional[float] = None

        # [Optional] Campaign Trigger Parameter
        self.trigger = None

        self.from_dict(kw)

    @property
    def id(self) -> int:
        """ Integer ID of the Observation in the Skynet database"""
        return self._id

    @property
    def type(self) -> str:
        """ Type of Observation. Always 'light' for non-Skynet developers """
        return self._type

    @property
    def state(self) -> str:
        """ State of the Observation (active or canceled) """
        return self._state

    @property
    def time_submitted_utc(self) -> str:
        """ Datetime that the Observation was stored in the Skynet database"""
        return self._time_submitted_utc

    def from_dict(self, d) -> None:
        """ Calls 'from_dict' from the super class and handles the
        cases for triggers.

        :param d: Key value pairing of attributes and values
        """
        super().from_dict(d)

        exposures, self.exps = d.get('exps'), []

        if exposures:
            for exposure in exposures:
                self.exps.append(Exposure(**exposure))

        if trigger := d.get('trigger'):
            self.trigger = Trigger(**trigger)
