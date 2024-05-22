from agridable.formats.value import Duration


def test_duration_init_default():
    duration = Duration()
    assert duration.unit == 'minutes'
    assert duration.output_unit == 'minutes'


def test_duration_init_custom():
    duration = Duration(unit='seconds', output_unit='hours')
    assert duration.unit == 'seconds'
    assert duration.output_unit == 'hours'


def test_duration_create_format_function_default():
    duration = Duration()
    expected_function = 'formatDuration(params.value, "minutes", "minutes")'
    assert duration._create_format_function() == expected_function


def test_duration_create_format_function_custom():
    duration = Duration(unit='hours', output_unit='minutes')
    expected_function = 'formatDuration(params.value, "hours", "minutes")'
    assert duration._create_format_function() == expected_function
