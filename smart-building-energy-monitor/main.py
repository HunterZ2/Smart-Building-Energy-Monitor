from src.sensors import VoltageSensor, CurrentSensor
from src.power import calculate_power
from src.analytics import energy_kwh
from src.alerts import check_alert

v = VoltageSensor().read()
i = CurrentSensor().read()

p = calculate_power(v, i)
e = energy_kwh(p, 24)

print("Smart Building Energy Monitor")
print(f"Voltage: {v:.2f} V")
print(f"Current: {i:.2f} A")
print(f"Power: {p:.2f} W")
print(f"Daily Energy: {e:.2f} kWh")

alert = check_alert(p)
if alert:
    print("ALERT:", alert)
