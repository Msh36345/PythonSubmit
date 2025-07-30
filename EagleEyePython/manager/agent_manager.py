from models.agent import Agent
from dal.agent_dal import AgentDal

class AgentManager:
    def __init__(self):
        self.dal = AgentDal()

    def create_agent(self):
        codeName=input("Enter code name : ")
        realName=input("Enter real name : ")
        location=self._choice_location()
        agent=Agent(codeName,realName,location)
        self.dal.add_agent(agent)
        print("\033[37m"+f"Agent {agent.code_name} created successfully.\033[0m")

    def update_agent_mission(self):
        agent = self._choice_agent()
        agent.mission_completed+=1
        self.dal.update_agent(agent)
        print("\033[37m"+f"Agent {agent.code_name} mission count updated.\033[0m")

    def update_agent_location(self):
        agent = self._choice_agent()
        new_location=self._choice_location()
        agent.location=new_location
        self.dal.update_agent(agent)
        print("\033[37m"+f"Agent {agent.code_name} location updated.\033[0m")

    def update_agent_status(self):
        agent = self._choice_agent()
        new_status=self._choice_status()
        agent.status = new_status
        if new_status=="Missing":
            agent.location="Unknown"
        if new_status=="Retired":
            agent.location="Unspecified"
        self.dal.update_agent(agent)
        print("\033[37m"+f"Agent {agent.code_name} status updated.\033[0m")


    def get_all_agents(self):
        return self.dal.get_agents()

    def get_agents_by_status(self):
        status=self._choice_status()
        agents=self.get_all_agents()
        not_found=True
        for agent in agents:
            if agent.status==status:
                print(agent)
                not_found=False
        if not_found:
            print(f"No agents found with status : {status}")

    def get_agents_by_location(self):
        location=self._choice_location()
        agents=self.get_all_agents()
        not_found=True
        for agent in agents:
            if agent.location==location:
                print(agent)
                not_found=False
        if not_found:
            print(f"No agents found in {location}")


    def _choice_agent(self):
        agents=self.get_all_agents()
        for i,agent in enumerate(agents):
            print(f"{i+1}. {agent}")
        choice=self._get_input_num(len(agents))
        return agents[choice-1]

    def _choice_status(self):
        status = ["Active", "Injured", "Missing", "Retired"]
        print("\033[32m" + """=========================================
|| 1. Active       || 3. Missing       ||
|| 2. Injured      || 4. Retired       ||
=========================================\033[0m""")
        choice = self._get_input_num(len(status))
        return status[choice-1]

    def _choice_location(self):
        locations = ["Israel", "Gaza", "Lebanon", "Iran", "Europe", "United States", "Unknown", "Unspecified"]
        print("\033[32m" + """=========================================
|| 1. Israel       || 5. Europe        ||
|| 2. Gaza         || 6. United States ||
|| 3. Lebanon      || 7. Unknown       ||
|| 4. Iran         || 8. Unspecified   ||
=========================================\033[0m""")
        choice = self._get_input_num(len(locations))
        return locations[choice-1]

    def _get_input_num(self,num):
        while True:
            try:
                choice=int(input("Enter your choice : "))
                if 0<choice<=num:
                    return choice
                else:
                    print(f"\033[31mInvalid number. Please enter a valid number between 1 and {num}\033[0m")
            except:
                print("\033[31mUnauthorized input. Please enter a number.\033[0m")