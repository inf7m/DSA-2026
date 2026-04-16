# DSA-2026
# Property Agency Commission System

## 📌 Overview
This project is a Python-based Object-Oriented system designed to simulate a property agency workflow. It models property agents and directors, manages property sales, and calculates commissions based on property value and commission sharing rules.

The system follows OOP principles such as inheritance, encapsulation, and modular design. Each class is separated into its own file for better maintainability and clarity.

---

## 📁 Project Structure

---
project

property.py # Base Property class

commercial_property.py # CommercialProperty (inherits Property)

property_agent.py # PropertyAgent class (manages properties & commission)

property_agency_director.py # Director class (inherits Agent, manages agents)

commission_slip.py # Handles commission report generation

main.py # Entry point of the program

---
## ⚙️ Features

- Manage property data (address, valuation, type, etc.)
- Separate sold and unsold properties for each agent
- Calculate agent commission based on:
  - Property valuation
  - Commission rate (default 1%)
  - Agent sharing rate (default 70%)
- Director override commission from agents
- Generate detailed commission slips for:
  - Agents
  - Directors

---

## ▶️ How to Run

### 1. Make sure Python is installed
```bash
python --version
