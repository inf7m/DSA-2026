from property_agent import PropertyAgent

class PropertyAgencyDirector(PropertyAgent):
    def __init__(self, name, reg_number, company, start_year,
                 sharing_rate=0.75, override_rate=0.05):
        super().__init__(name, reg_number, company, start_year, sharing_rate)
        self.override_rate = override_rate
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def calculate_override_income(self):
        total = 0
        breakdown = []

        for agent in self.agents:
            agent_commission, _ = agent.calculate_commission()
            override = agent_commission * self.override_rate
            breakdown.append((agent.name, override))
            total += override

        return total, breakdown
