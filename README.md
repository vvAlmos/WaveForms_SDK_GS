Demo package for the WaveForms SDK Getting Started guide and multiple test scripts for different instruments.

Check: https://digilent.com/reference/test-and-measurement/guides/waveforms-sdk-getting-started for more details.

Available tests:
    - empty test template
    - analog signal generation and recording test
    - digital signal generation and recording test
    - blinking LEDs with the Suplpies and the Static I/O instruments
    - UART in/out test using the Pmod CLS and the Pmod MAXSonar
    - SPI in/out test using the Pmod CLS and the Pmod ALS
    - I2C in/out test using the Pmod CLS and the Pmod TMP2

Available instruments and functions:
    - device
        - open
        - check_error
        - close
    - oscilloscope
        - open
        - measure
        - trigger
        - record
        - close
    - waveform generator
        - generate
        - close
    - power supplies
        - switch
        - switch_fixed (for Analog Discovery)
        - switch_variable (for Analog Discovery 2 and Studio)
        - switch_digital (for Digital Discovery and Analog Discovery Pro 3X50)
        - switch_6V (for Analog Discovery Pro 5250)
        - switch_25V (for Analog Discovery Pro 5250)
        - close
    - digital multimeter
        - open
        - measure       * UNTESTED *
        - close
    - logic analyzer
        - open
        - trigger
        - record
        - close
    - pattern generator
        - generate
        - close
    - static I/O
        - set_mode
        - get_state
        - set_state
        - set_current   * UNTESTED *
        - set_pull      * UNTESTED *
        - close
    - protocol: UART
        - open
        - read
        - write
        - close
    - protocol: SPI
        - open
        - read
        - write
        - echange
        - spy           * UNTESTED *
        - close
    - protocol: I2C
        - open
        - read
        - write
        - echange
        - spy           * UNTESTED *
        - close
