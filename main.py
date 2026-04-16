from property_agent import PropertyAgent
from property_agency_director import PropertyAgencyDirector
from property import Property
from commission_slip import CommissionSlip


def create_properties(n):
    props = []
    for i in range(n):
        props.append(Property(
            address=f"Street {i}",
            postal_code=100000 + i,
            tenure="Freehold",
            completion_year=2000,
            property_type="Condo",
            area=120,
            valuation=1000000 + i * 50000
        ))
    return props


# =======================
# CREATE DIRECTORS
# =======================
director1 = PropertyAgencyDirector("Director A", "D001", "ABC", 2015)
director2 = PropertyAgencyDirector("Director B", "D002", "XYZ", 2016)

# =======================
# CREATE AGENTS
# =======================
agents = [
    PropertyAgent("Agent 1", "A001", "ABC", 2020),
    PropertyAgent("Agent 2", "A002", "ABC", 2020),
    PropertyAgent("Agent 3", "A003", "ABC", 2020),
    PropertyAgent("Agent 4", "A004", "XYZ", 2020),
    PropertyAgent("Agent 5", "A005", "XYZ", 2020),
    PropertyAgent("Agent 6", "A006", "XYZ", 2020),
]

director1.agents = agents[:3]
director2.agents = agents[3:]

# =======================
# ASSIGN PROPERTIES
# =======================
for agent in agents:
    unsold = create_properties(5)
    sold = create_properties(5)

    for p in unsold:
        agent.add_unsold(p)

    for p in sold:
        agent.add_unsold(p)
        agent.sell_property(p)

# =======================
# PRINT SLIPS
# =======================
for agent in agents:
    CommissionSlip.print_agent(agent)

CommissionSlip.print_director(director1)
CommissionSlip.print_director(director2)
