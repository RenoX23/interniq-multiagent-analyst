print("Starting...")

from agents.sql_agent import run_sql_agent
print("SQL agent imported")

out = run_sql_agent('What are the top 10 most in-demand skills?')
print("SQL done. Rows:", len(out['results']))
print("Error:", out['error'])

from agents.viz_agent import run_viz_agent
fig = run_viz_agent(out['results'], out['question'])
print("Viz done. Fig:", type(fig))

from agents.insight_agent import run_insight_agent
print("Calling insight agent...")
insight = run_insight_agent(out['question'], out['sql'], out['results'])
print("Insight:", insight)
