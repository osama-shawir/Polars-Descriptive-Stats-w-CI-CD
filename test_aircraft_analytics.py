# -*- coding: utf-8 -*-

"""
TESTS goes here
"""
from aircraft_analytics import AircraftAnalytics

def test_aircraft_analytics():
    """ This is a function to test our AircraftAnalytics Function"""
    strikes, max_damaged_part = AircraftAnalytics()
    # Check if the calculated values meet expectations
    assert isinstance(strikes, dict)
    assert max_damaged_part in strikes
    assert max_damaged_part == max(strikes, key=strikes.get)
