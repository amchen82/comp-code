from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color, Button
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.D)

# Map detected colors -> program file to run
COLOR_TO_FILE = {
    Color.GREEN: "redsiderun1.py",
    Color.BLUE: "bluesiderun1.py",
    Color.RED: "totheotherworld.py",
    Color.YELLOW: "redsiderun2.py",
    Color.MAGENTA: "Arm_Test_DOCTOR.py",
    Color.BLACK: "forum.py",
    Color.ORANGE: "RuN-AwAy_CArROTs.py",
}

def wait_for_any_mapped_color():
    """Wait until the sensor sees one of the colors in COLOR_TO_FILE."""
    while True:
        # h, s, v = sensor.hsv()
        light = sensor.reflection()
        c = sensor.color()
        # print("Detected color:", c)
        # Magenta detection using HSV values
        # if 280 <= h <= 320 and s > 50:
            # return Color.MAGENTA
        if 45 <= light <= 55:
            return Color.ORANGE
        if light < 30: # Treat very low light as BLACK
            return Color.BLACK
        if c in COLOR_TO_FILE:
            return c
        wait(20)

def wait_for_right_button_click():
    """Wait for a clean RIGHT button click (press + release)."""
    # Wait for press
    while Button.RIGHT not in hub.buttons.pressed():
        wait(20)
    # Wait for release (debounce)
    while Button.RIGHT in hub.buttons.pressed():
        wait(20)

def run_file(filename):

    with open(filename, "r") as f:
        code = f.read()
    exec(code, globals())

while True:
    print("Show RED / BLUE / GREEN to select Run 1/2/3...")

    detected = wait_for_any_mapped_color()

    # Change hub light to match the detected color
    hub.light.on(detected)
    print("Detected color:", detected)

    selected_file = COLOR_TO_FILE[detected]
    print("Selected:", selected_file)
    print("Press RIGHT button to start...")

    wait_for_right_button_click()

    # print("Running:", selected_file)
    # run_file(selected_file)

    hub.light.off()

    # Small pause before allowing another selection
    wait(200)