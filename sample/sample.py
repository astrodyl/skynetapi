import json

import api.request.obs as ObservationRequest


if __name__ == '__main__':

    token = '1234'  # Access your Skynet API token

    # _________________________________________________________________
    #                     [ Add an observation ]
    # -----------------------------------------------------------------
    obs = ObservationRequest.add(
        token=token,
        **{'name': 'api-test',
           'mode': 1, 'timeAccountId': 456, 'targetTracking': 'track_target',
           'raHours': 12., 'decDegs': 40.,  # Coordinates
           'minEl': 20, 'maxSun': -18, 'minMoonSepDegs': 0,  # Observing Constraints
           'exps': json.dumps([dict(expLength=5, filterRequested='R', telescopeRequested='Morehead')])})

    # _________________________________________________________________
    #                   [ Cancel an observation ]
    # -----------------------------------------------------------------
    obs = ObservationRequest.cancel(token=token, obs_id=obs.id)

    # _________________________________________________________________
    #          [ Query all observation after provided date ]
    # -----------------------------------------------------------------
    obs_ids = ObservationRequest.get(token=token, **{'after': '2024-08-28T12:00:00'})

    # _________________________________________________________________
    #         [ Add an observation using the Campaign Manager ]
    # -----------------------------------------------------------------
    cm_obs = ObservationRequest.add(
        token=token,
        **{'name': 'cm-api-test',

           # Observation parameters
           'mode': 2, 'targetTracking': 'track_target', 'raHours': 15., 'decDegs': 25.,
           'minEl': 20, 'maxSun': -18, 'minMoonSepDegs': 0,

           # Campaign Trigger parameters
           'trigger': {
               'campaign_id': 123,
               'reference_mag': 20.0,
               'reference_time': 3600.0,
               'reference_filter': 'R',

               'delay': 0.0,
               'desired_snr': 10.0,
               'temporal_model': 'power',

               'event_time': '2023-04-15T05:20:00.0',
               'temporal_index': -1,
               'spectral_index': -0.7,
               'dust_extinction': 0.0,
                }
           }
    )
