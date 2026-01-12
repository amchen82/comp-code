from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button,Color

hub = PrimeHub()

selected = hub_menu("1","2","3","4","5","6", "7")
hub.system.set_stop_button(Button.CENTER)

hub.light.on(Color.BLUE)

if selected == "1":
    import redsiderun1
elif selected == "2":
    import redsiderun2
elif selected == "3":
    import redsiderun3
elif selected == "4":
    import bluesiderun2
elif selected == "5":
    import bluesiderun1
elif selected == "6":
    import final
elif selected == "7":
    import final_2