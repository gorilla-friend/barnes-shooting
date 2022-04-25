
import json
from nba_api.stats.endpoints import shotchartdetail
import pandas as pd

response = shotchartdetail.ShotChartDetail( 
        team_id=0,
        player_id=1630567, # Scottie Barnes
        season_nullable="2021-22",
        season_type_all_star="Regular Season"
)

content = json.loads(response.get_json())

# Transform content to dataframe
results = content["resultSets"][0]
headers = results["headers"]
rows = results["rowSet"]
df = pd.DataFrame(rows)
df.columns = headers

# Convert to CSV
df.to_csv("barnes-shooting.csv", index=False)