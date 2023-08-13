import serial
import time

# Define the serial port and baud rate
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

# Initialize the serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

def set_servo_position(servo_number, angle):
    command = f"{servo_number}:{angle}\n"
    ser.write(command.encode())

def main():
    try:
        while True:
            for servo in range(1, 6):
                angle = int(input(f"Enter angle for servo {servo}: "))
                set_servo_position(servo, angle)
    except KeyboardInterrupt:
        print("Exiting")
        ser.close()

if __name__ == "__main__":
    main()
