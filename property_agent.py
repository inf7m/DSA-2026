class PropertyAgent:
    def __init__(self, name, reg_number, company, start_year, sharing_rate=0.70):
        self.name = name
        self.reg_number = reg_number
        self.company = company
        self.start_year = start_year
        self.sharing_rate = sharing_rate

        self.unsold_properties = []
        self.sold_properties = []

    def add_unsold(self, prop):
        self.unsold_properties.append(prop)

    def sell_property(self, prop):
        if prop in self.unsold_properties:
            self.unsold_properties.remove(prop)
            self.sold_properties.append(prop)

    def calculate_commission(self):
        total = 0
        breakdown = []

        for p in self.sold_properties:
            commission = p.valuation * p.commission_rate * self.sharing_rate
            breakdown.append((p.address, commission))
            total += commission

        return total, breakdown
