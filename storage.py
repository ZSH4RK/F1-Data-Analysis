# Seasons you want
seasons = [2019, 2020, 2021, 2022, 2024]

all_season_scores = []

for season in seasons:
    # Filter season
    season_results = results[results['Season'] == season].reset_index(drop=True)

    # Group by cluster and driver
    driver_scores = season_results.groupby(['DriverNumber', 'cluster']).agg(
        AvgDriverQualiTime=('MinQualiTime', 'mean'),
        StdDriverQualiTime=('MinQualiTime', 'std'),
        AvgTeamQualiTime=('TeamAvgQualiTime', 'mean'),
        AvgOverallQualiTime=('MinOverallQualiTime', 'mean'),
        RacesCount=('RoundNumber', 'count'),
        TeamName=('TeamName', 'max'),
        StdNormLapTime=('NormalizedLapTime', 'std'),
        AvgNormLapTime=('NormalizedLapTime', 'mean')
    ).reset_index()

    # Compute raw scores
    driver_scores['PaceScore'] = 2.71828**(
        -0.5 * (driver_scores['AvgDriverQualiTime'] - driver_scores['AvgOverallQualiTime'])
    )

    k = 100
    driver_scores['ConsistencyScore'] = 1 / (
        1 + k * driver_scores['StdNormLapTime'] / driver_scores['AvgNormLapTime']
    )

    # Add season column
    driver_scores['Season'] = season

    # Store results
    all_season_scores.append(driver_scores)

# Combine all seasons into one DataFrame
season_scores = pd.concat(all_season_scores, ignore_index=True)
