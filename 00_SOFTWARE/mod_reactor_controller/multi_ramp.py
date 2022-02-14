from mod_reactor_controller.koradserial import KoradSerial
import sys
import serial
import platform


def init_KoradSerial(**kwargs):
    voltage = float(input("Voltage? "))  # set operating voltage

    KoradSerial.device = KoradSerial(port=kwargs['port'], baudrate=kwargs['baudrate'], timeout=kwargs['timeout'],
                                     parity=kwargs['parity'], rtscts=kwargs['rtscts'],
                                     debug=False
                                     )
    channel = KoradSerial.device.channels[0]
    m1 = KoradSerial.device.memories[0]
    KoradSerial.device.beep.off()

    channel.voltage = voltage
    return [KoradSerial, channel]


def set_ramp():
    list_x1 = []  # List with coordinates of the starting time of the ramp
    list_x2 = []  # List with coordinates of the ending time of the ramp
    list_y1 = []  # List with coordinates of the starting current of the ramp
    list_y2 = []  # List with coordinates of the ending current of the ramp

    while True:

        x1 = float(input("time of the first point in seconds = "))  # input of ramp coordinates
        y1 = float(input("current of the first point in ampere = "))  # input of ramp coordinates
        x2 = float(input("time of the second point in seconds = "))  # input of ramp coordinates
        y2 = float(input("current of the second point in ampere = "))  # input of ramp coordinates

        list_x1.append(x1)
        list_x2.append(x2)
        list_y1.append(y1)
        list_y2.append(y2)

        add_Ramp = input("add ramp? (y/press key to interrupt)")

        if add_Ramp == "y":
            print("add additional ramp values")

        if add_Ramp != "y":
            break

    return [list_x1, list_x2, list_y1, list_y2]


def intensity_ramp(channel, ramp_list, t, device):
    """
    Parameters
    ----------
    slope : int or float
        Value for calculated slope of the linear function.

    y_intercept : int or float
        Value for calculated  y-axis intercept of the linear function.

    calc_current : int or float
        Value for calculated  current derived from the linear function for a certain point in time.
    """
    for x1, x2, y1, y2 in zip(*ramp_list):

        while x1 <= t < x2:
            slope = (y1 - y2) * 1.0 / (x1 - x2)  # !!!attention division!!!
            y_intercept = (x1 * y2 - x2 * y1) * 1.0 / (x1 - x2)
            calc_current = slope * t + y_intercept
            channel.current = abs(calc_current)
            device.device.output.on()
            t += 0.225  # this is the delay time of the power supply
            print(t)
    device.device.output.off()
    device.device.close()
    quit()


def start(**kwargs):
    if kwargs == {}:
        if platform.system() == "Windows":  # standard settings for windows
            port = 'COM3'
            baudrate = 38400
            timeout = 0
            parity = serial.PARITY_EVEN
            rtscts = True
        if platform.system() == "Linux":  # standard settings for linux
            port = '/dev/ttyACM0'
            baudrate = 9600
            timeout = 1
            parity = serial.PARITY_NONE
            rtscts = False
    else:
        port = kwargs['port']
        baudrate = kwargs['baudrate']
        timeout = kwargs['timeout']
        parity = kwargs['parity']
        rtscts = kwargs['rtscts']
    t = 0  # start time 0 s (value can be int or float)
    device, channel = init_KoradSerial(port=port, baudrate=baudrate, timeout=timeout, parity=parity, rtscts=rtscts)
    ramp = set_ramp()
    intensity_ramp(channel, ramp, t, device)

    quit()


if __name__ == "__main__":
    if sys.argv:
        port, baudrate, timeout = sys.argv
    else:  # settings for windows
        port = 'COM3'
        baudrate = 38400
        timeout = 0
        parity = serial.PARITY_EVEN
        rtscts = 1
