from gpiozero import Servo

# Position "0" (1.5 ms pulse) is middle, "90" (~2ms pulse) is middle, is all the way to the right, "-90" (~1ms pulse) is all the way to the left.
servo = Servo(18, min_pulse_width = 1.0/1000, max_pulse_width = 2.0/1000)

