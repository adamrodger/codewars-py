from codewars.kyu5.human_readable_duration import format_duration
from nose.tools import assert_equal

def test_now():
    assert_equal(format_duration(0), "now")

def test_seconds():
    yield assert_equal, format_duration(1), "1 second"
    yield assert_equal, format_duration(2), "2 seconds"
    yield assert_equal, format_duration(10), "10 seconds"
    yield assert_equal, format_duration(59), "59 seconds"

def test_minutes():
    yield assert_equal, format_duration(60), "1 minute"
    yield assert_equal, format_duration(120), "2 minutes"
    yield assert_equal, format_duration(61), "1 minute and 1 second"
    yield assert_equal, format_duration(62), "1 minute and 2 seconds"
    yield assert_equal, format_duration(121), "2 minutes and 1 second"
    yield assert_equal, format_duration(122), "2 minutes and 2 seconds"

def test_hours():
    yield assert_equal, format_duration(3600), "1 hour"
    yield assert_equal, format_duration(7200), "2 hours"
    yield assert_equal, format_duration(7201), "2 hours and 1 second"
    yield assert_equal, format_duration(7202), "2 hours and 2 seconds"
    yield assert_equal, format_duration(7261), "2 hours, 1 minute and 1 second"
    yield assert_equal, format_duration(7262), "2 hours, 1 minute and 2 seconds"
    yield assert_equal, format_duration(7321), "2 hours, 2 minutes and 1 second"
    yield assert_equal, format_duration(7322), "2 hours, 2 minutes and 2 seconds"

def test_days():
    yield assert_equal, format_duration(86400), "1 day"
    yield assert_equal, format_duration(90000), "1 day and 1 hour"
    yield assert_equal, format_duration(90001), "1 day, 1 hour and 1 second"
    yield assert_equal, format_duration(90061), "1 day, 1 hour, 1 minute and 1 second"
    yield assert_equal, format_duration(172800), "2 days"

def test_years():
    yield assert_equal, format_duration(31536000), "1 year"
    yield assert_equal, format_duration(31536001), "1 year and 1 second"
    yield assert_equal, format_duration(31536061), "1 year, 1 minute and 1 second"
    yield assert_equal, format_duration(31539661), "1 year, 1 hour, 1 minute and 1 second"
    yield assert_equal, format_duration(31626061), "1 year, 1 day, 1 hour, 1 minute and 1 second"
    yield assert_equal, format_duration(63072000), "2 years"