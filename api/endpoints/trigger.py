from datetime import datetime

from api.endpoints.endpoint import Endpoint


class Trigger(Endpoint):
    def __init__(self, **kw):
        super().__init__()

        self._id: int | None = None                      # Integer ID of the Trigger object

        # [Required] Reference Parameters
        self.reference_mag: float | None = None         # Magnitude of target in reference image
        self.reference_time: float | None = None        # Time that the reference image was taken
        self.reference_filter: str | int | None = None  # Filter used in the reference image

        # [Required] Observer Defined Parameters
        self.campaign_id: int | None = None             # Integer ID of the Campaign Template
        self.delay: float | None = None                 # Delay in seconds between filter sequences
        self.desired_snr: float | None = None           # Desired signal-to-noise ratio of the target
        self.temporal_model: str | None = None          # Power Law or Exponential

        # [Required] Observing Parameters
        self.event_time: datetime | None = None         # Time of the event trigger
        self.temporal_index: float | None = None        # Temporal evolution (negative indicates fading)
        self.spectral_index: float | None = None        # Spectral evolution (negative indicates fading)
        self.dust_extinction: float = 0.0               # E(B - V)

        self.from_dict(kw)

    @property
    def id(self):
        """ Integer ID of the Campaign Trigger in the Skynet database """
        return self._id
