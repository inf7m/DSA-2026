class CommissionSlip:

    @staticmethod
    def print_agent(agent):
        total, breakdown = agent.calculate_commission()

        print(f"\n===== AGENT COMMISSION: {agent.name} =====")
        for addr, c in breakdown:
            print(f"{addr}: ${c:.2f}")
        print(f"TOTAL: ${total:.2f}")

    @staticmethod
    def print_director(director):
        print(f"\n===== DIRECTOR COMMISSION: {director.name} =====")

        agent_total = 0

        for agent in director.agents:
            CommissionSlip.print_agent(agent)
            agent_total += agent.calculate_commission()[0]

        override_total, breakdown = director.calculate_override_income()

        print("\n--- OVERRIDE INCOME ---")
        for name, val in breakdown:
            print(f"{name}: ${val:.2f}")

        print(f"TOTAL OVERRIDE: ${override_total:.2f}")
        print(f"TOTAL DIRECTOR INCOME: ${agent_total + override_total:.2f}")
