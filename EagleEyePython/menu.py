from manager.agent_manager import AgentManager
import time

manager = AgentManager()

def menu():
    print("\033[96m" + """============================================
||  👋 Welcome to the Eagle Eye Project!  ||
============================================""" + "\033[0m")
    time.sleep(2)

    while True:
        print("""\033[93m=========================
||     Main Menu       ||
=========================
||    1.Create Agent   ||
||    2.Update Agent   ||
||    3.View Agents    ||
||    4.Exit           ||
=========================\033[0m""")
        choice=manager._get_input_num(4)

        match choice:
            case 1:
                manager.create_agent()
            case 2:
                update_menu()
            case 3:
                wiew_menu()
            case 4:
                print("\033[96m" + """
=======================
||   👋 Bye Bye 👋   ||
=======================""" + "\033[0m")
                break
def update_menu():
    while True:
        print("""\033[94m
=========================
||     Update Menu     ||
=========================
||  1.Update Mission   ||
||  2.Update Location  ||
||  3.Update Status    ||
||  4.Back             ||
=========================\033[0m""")
        choice = manager._get_input_num(4)

        match choice:
            case 1:
                manager.update_agent_mission()
            case 2:
                manager.update_agent_location()
            case 3:
                manager.update_agent_status()
            case 4:
                break
def wiew_menu():
    while True:
        print("""\033[94m
===============================
||        View Menu          ||
===============================
||  1.View All Agents        ||
||  2.View Agent By Status   ||
||  3.View Agent By Location ||
||  4.Back                   ||
===============================\033[0m""")
        choice = manager._get_input_num(4)

        match choice:
            case 1:
                agents=manager.get_all_agents()
                for agent in agents:
                    print(agent)
            case 2:
                manager.get_agents_by_status()
            case 3:
                manager.get_agents_by_location()
            case 4:
                break

if __name__ == "__main__":
    menu()
