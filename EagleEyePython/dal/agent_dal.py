import mysql.connector

class AgentDal:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="eagleEyePython")

    def add_agent(self, agent):
        query = "INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES (%s, %s, %s, %s, %s)"
        values = (agent.code_name, agent.real_name, agent.location, agent.status, agent.mission_completed)
        with self.db.cursor() as cursor:
            cursor.execute(query, values)
            self.db.commit()

    def update_agent(self,agent):
        query = "UPDATE agents SET codeName=%s, realName=%s, location=%s, status=%s, missionsCompleted=%s WHERE id=%s"
        values = (agent.code_name, agent.real_name, agent.location, agent.status, agent.mission_completed, agent.id)
        with self.db.cursor() as cursor:
            cursor.execute(query, values)
            self.db.commit()

    def get_agents(self):
        from models.agent import Agent
        agents=[]
        query = "SELECT * FROM agents"
        with self.db.cursor() as cursor:
            cursor.execute(query)
            for line in cursor.fetchall():
                agents.append(Agent(line[1],line[2],line[3],id=line[0],status=line[4],mission_completed=line[5]))
        return agents
