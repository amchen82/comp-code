from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button,Color

hub = PrimeHub()

selected = hub_menu("1","2","3","4","5","6", "7")
hub.system.set_stop_button(Button.CENTER)

hub.light.on(Color.BLUE)

if selected == "3":
    import redmission11and12
elif selected == "2":
    import redmission3and4
elif selected == "1":
    import redmission1and2
elif selected == "5":
    import new_silo
elif selected == "6":
    import Simple_Artifact_Dump
elif selected == "4":
    import TIPtheSCALESthingy
elif selected == "7":
    import TiPtheScALeTHiNGy2