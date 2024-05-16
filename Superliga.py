# realizare matrice rezultate - campionat regulat, play-off, play-out
import pandas as pd

# print("\nCampionat regulat:")
campionatRegulat = pd.read_excel('campionat_regulat.xlsx', sheet_name='WDL', index_col='HOME')
rezultateCampionatRegulat = pd.read_excel('campionat_regulat.xlsx', sheet_name='Score', index_col='HOME')
homeTeams = campionatRegulat.index
awayTeams = campionatRegulat.columns

winners = {team: {} for team in homeTeams}

for homeTeam in homeTeams:
    for awayTeam in awayTeams:
        winner = 'undefined'
        loser = 'undefined'
        result = campionatRegulat[awayTeam][homeTeam]
        score = rezultateCampionatRegulat[awayTeam][homeTeam]
        if result == 'X' or result == 'D':
            continue
        else:
            if result == 'W':
                winner = homeTeam
                loser = awayTeam
            if result == 'L':
                winner = awayTeam
                loser = homeTeam
            if winner != 'undefined' and loser != 'undefined':
                winners[winner][loser] = score

# print("\nPlay-off:")
playoff = pd.read_excel('play_off.xlsx', sheet_name="WDL", index_col="HOME")
rezultatePlayoff = pd.read_excel("play_off.xlsx", sheet_name="Score", index_col="HOME")

# print("\nPlay-out:")
playout = pd.read_excel('play_out.xlsx', sheet_name="WDL", index_col="HOME")
rezultatePlayout = pd.read_excel("play_out.xlsx", sheet_name="Score", index_col="HOME")

for k, v in winners.items():
    print("\n", k, ":", v)
