import temperature_sensor


def get_current_temperature():
    """
    get temperature reading from temperature_sensor
    determine temperature and display weather condition
    :return: weather condition
    """
    current_temp = temperature_sensor.read_temperature()
    if 70 < current_temp < 80:
        return f"Nice weather, {current_temp}F!"
    if current_temp < 0:
        raise SystemError
    return f"Rough weather, {current_temp}F!"
