from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button,Color

hub = PrimeHub()

selected = hub_menu("1","2","3","4","5","6", "7")
hub.system.set_stop_button(Button.CENTER)

hub.light.on(Color.BLUE)

if selected == "4":
    import arm_test_DOCTOR
elif selected == "5":
    import redsiderun2
elif selected == "6":
    import redsiderun3
elif selected == "2":
    import bluesiderun2
elif selected == "1":
    import bluesiderun1
elif selected == "3":
    import fromBlueToRed
elif selected == "7":
    import final_2