import minimalmodbus
import sqlite3
import time

# --- Setup the Modbus instrument ---
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # Adjust tty path and slave ID as needed
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity   = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1  # seconds
instrument.mode = minimalmodbus.MODE_RTU

# --- Read Energy registers (low + high) ---
try:
    energy_low = instrument.read_register(0x0005, 0, 3)   # Address, decimals, function code
    energy_high = instrument.read_register(0x0006, 0, 3)
    total_energy_wh = (energy_high << 16) + energy_low   # Combine 2x 16-bit registers into 1x 32-bit integer

    print(f"Energy: {total_energy_wh} Wh")

    # --- Save to SQLite database ---
    conn = sqlite3.connect('energy_data.db')
    c = conn.cursor()

    c.execute("INSERT INTO energy_log (energy_wh) VALUES (?)", (total_energy_wh,))
    conn.commit()
    conn.close()

    print("✅ Data logged to database.")

except Exception as e:
    print("Error reading from meter or logging to DB:", e)
