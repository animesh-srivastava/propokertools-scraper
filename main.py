from propokertools import run_query

query1 = """
select count(equity(tens, flop) > 0.33) as decent_equity
from game="holdem", tens="TT", villainOne="15%", villainTwo="15%"
"""

query2 = """
select histogram(equity(rundown, flop)) as flop,
       histogram(equity(rundown, turn)) as turn
from game="omahahi", rundown="TJ98", randomPlayer="****"
"""

query3 = """
select avg(
    case
      when equity(villain, preflop) * (4 + 10 *2) - 10 > 0
      then equity(hero, preflop) * (4 + 10 *2) - 10 - 1
      else 3
    end
  ) as hero_net_chips
from game="holdem", hero="22", villain="**"
"""

res = run_query(query1)
print(res)

res = run_query(query2)
print(res)

res = run_query(query3)
print(res)
