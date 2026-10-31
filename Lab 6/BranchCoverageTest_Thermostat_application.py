import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert


def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_before_six():
    assert target_temperature("sleep", True, 2) == 18


def test_sleep_mode_after_twenty_two():
    assert target_temperature("sleep", True, 23) == 18


def test_sleep_mode_daytime():
    assert target_temperature("sleep", True, 12) == 20


def test_unoccupied():
    assert target_temperature("home", False, 12) == 18


def test_morning_branch():
    assert target_temperature("home", True, 7) == 22


def test_evening_branch():
    assert target_temperature("home", True, 18) == 21


def test_default_temperature_branch():
    assert target_temperature("home", True, 12) == 20


def test_hvac_idle_branch():
    assert hvac_action(20, 20.5, 10) == "idle"


def test_hvac_heat_boost_branch():
    assert hvac_action(18, 22, 2) == "heat_boost"


def test_hvac_heat_branch():
    assert hvac_action(18, 22, 10) == "heat"


def test_hvac_cool_boost_branch():
    assert hvac_action(24, 20, 35) == "cool_boost"


def test_hvac_cool_branch():
    assert hvac_action(24, 20, 20) == "cool"


def test_energy_empty_list_branch():
    assert energy_alert([], 10) == "ok"


def test_energy_zero_over_limit_branch():
    assert energy_alert([8, 9, 10], 10) == "ok"


def test_energy_critical_branch():
    assert energy_alert([11, 12], 10) == "critical"


def test_energy_warning_branch():
    assert energy_alert([11, 9], 10) == "warning"