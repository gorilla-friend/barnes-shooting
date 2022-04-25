# https://github.com/swar/nba_api
# https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints

import json
from nba_api.stats.endpoints import shotchartdetail, playercareerstats
import pandas as pd

def json_to_df(response):

    # Turn json response into object
    content = json.loads(response.get_json())

    # Transform content to dataframe
    results = content["resultSets"][0]
    headers = results["headers"]
    rows = results["rowSet"]
    df = pd.DataFrame(rows)
    df.columns = headers

    return df

if __name__ == "__main__":

    response = shotchartdetail.ShotChartDetail (
        team_id=0,
        player_id=1630567, # Scottie Barnes
        season_nullable="2021-22",
        season_type_all_star="Regular Season"
    )
    # Transform to df
    ShotChart_df = json_to_df(response)
    # Convert to CSV
    ShotChart_df.to_csv("barnes-shotchartdetail.csv", index=False)

    response = playercareerstats.PlayerCareerStats (
        player_id=1630567, # Scottie Barnes

    )
    # Transform to df
    CommonInfo_df = json_to_df(response)
    # Convert to CSV
    CommonInfo_df.to_csv("barnes-careerstats.csv", index=False)



