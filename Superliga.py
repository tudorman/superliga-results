import pandas as pd

print("\nCampionat regulat:")
campionatRegulat = pd.read_excel('campionat_regulat.xlsx', sheet_name='WDL', index_col='HOME')
rezultateCampionatRegulat = pd.read_excel('campionat_regulat.xlsx', sheet_name='Score', index_col='HOME')
homeTeams = campionatRegulat.index
awayTeams = campionatRegulat.columns

winners = {team: {} for team in homeTeams}


def reorder_score(score):
    parts = score.split('-')
    first, second = int(parts[0]), int(parts[1])
    if first < second:
        return f"{second}-{first}"
    return score


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
                winners[winner][loser] = reorder_score(score)


def print_tree(current_team, teams_dict, visited=None, path=None, scores=None, longest_path=None, longest_scores=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if scores is None:
        scores = []
    if longest_path is None:
        longest_path = []
    if longest_scores is None:
        longest_scores = []

    path.append(current_team)
    visited.add(current_team)

    if len(path) > len(longest_path):
        longest_path.clear()
        longest_scores.clear()
        longest_path.extend(path)
        longest_scores.extend(scores)

    for next_team in teams_dict.get(current_team, {}):
        if next_team not in visited:
            score = reorder_score(teams_dict[current_team][next_team])
            scores.append(score)
            print_tree(next_team, teams_dict, visited, path, scores, longest_path, longest_scores)
            scores.pop()

    path.pop()
    visited.remove(current_team)

    if not path:
        if len(longest_path) > 1:
            formatted_path = []
            for i in range(len(longest_path) - 1):
                formatted_path.append(f"{longest_path[i]} ({longest_scores[i]})")
            formatted_path.append(longest_path[-1])
            print(" - ".join(formatted_path))


for winner in winners:
    print_tree(winner, winners)
