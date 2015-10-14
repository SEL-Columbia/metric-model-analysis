#!/usr/bin/env python
from sympy import *

# Example for solving total_cost equation for demand
total, demand, cost_per_kw, gen_cost, inst_cost_fraction = \
symbols('total demand cost_per_kw gen_cost inst_cost_fraction')

expr = demand * cost_per_kw + gen_cost * inst_cost_fraction
demand_expr = solve(expr - total, demand)
print(demand_expr)
# >>> [(-gen_cost*inst_cost_fraction + total)/cost_per_kw]
