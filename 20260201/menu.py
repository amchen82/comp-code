from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button,Color

hub = PrimeHub()

selected = hub_menu("1","2","3","4","5","6", "7")
hub.system.set_stop_button(Button.CENTER)

hub.light.on(Color.BLUE)

if selected == "4":
    import mission11and12
elif selected == "5":
    import mission3and4
elif selected == "6":
    import mission1and2
elif selected == "1":
    import mission5678
elif selected == "2":
    import mission9and10
elif selected == "3":
    import fromBlueToRed
elif selected == "7":
    import pushArtifacts