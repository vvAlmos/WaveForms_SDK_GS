""" IMPORT ISNTRUMENT FUNCTIONS """

import dwfconstants as constants  # import every constant
import device                     # device control functions
import scope                      # oscilloscope control functions
import wavegen                    # waveform generator control functions

import matplotlib.pyplot as plt   # needed for plotting

"""-----------------------------------------------------------------------"""

""" MAIN PROGRAM """

# connect to the device
device_handle = device.open()

# check for connection errors
device.check_error(device_handle)

# initialize the scope with default settings
scope.open(device_handle)

# set up triggering on scope channel 1
scope.trigger(device_handle, enable=True, source=constants.trigsrcDetectorAnalogIn, channel=0, level=0)

# generate a 10KHz sine signal with 2V amplitude on channel 1
wavegen.generate(device_handle, channel=1, function=constants.funcSine, offset=0, frequency=10e03, amplitude=2)

# record data with the scopeon channel 1
buffer, time = scope.record(device_handle, channel=1)

# plot
time = [moment * 1e03 for moment in time]   # convert time to ms
plt.plot(time, buffer)
plt.xlabel("time [ms]")
plt.ylabel("voltage [V]")
plt.show()

# reset the scope
scope.close(device_handle)

# reset the wavegen
wavegen.close(device_handle)

# close the connection
device.close(device_handle)
