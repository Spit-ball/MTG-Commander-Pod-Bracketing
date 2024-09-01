import random
from collections import defaultdict

# Get Player Names
def get_player_names():
    players = []
    while True:
        player_name = input("Enter player name (or type 'complete' to finish): ")
        if player_name.lower() == "complete":
            break
        if player_name:  # Ensure the player name is not empty
            players.append(player_name)
    return players

# Determine pod sizes based on number of players
def determine_pod_sizes(num_players):
    if num_players % 4 == 0 or num_players % 4 == 3:
        return [4] * (num_players // 4) + ([3] if num_players % 4 == 3 else [])
    elif num_players % 5 == 0 or num_players % 5 == 4:
        return [5] * (num_players // 5) + ([4] if num_players % 5 == 4 else [])
    else:
        return [4] * (num_players // 4) + [3] * ((num_players % 4) // 3) + [5] * ((num_players % 4) // 5)

# Create pods for the first round
def create_initial_pods(players):
    pod_sizes = determine_pod_sizes(len(players))
    random.shuffle(players)
    pods = []
    start = 0
    for size in pod_sizes:
        pods.append(players[start:start + size])
        start += size
    return pods

# Update scores after a round
def update_scores(pods, results, scores):
    for pod, result in zip(pods, results):
        for i, player in enumerate(result):
            scores[player] += len(pod) - i  # Example: 3 points for 4th place in a 4-player pod
    return scores

# Calculate sum of opponents' scores for tiebreaker
def sum_opponents_scores(player, previous_pods, scores):
    opponent_scores = 0
    for pod in previous_pods:
        if player in pod:
            opponent_scores += sum(scores[opponent] for opponent in pod if opponent != player)
    return opponent_scores

# Sort players using primary and secondary tiebreaker
def sort_players(players, scores, previous_pods):
    return sorted(players, key=lambda x: (scores[x], sum_opponents_scores(x, previous_pods, scores)), reverse=True)

# Check if a rematch is happening
def is_rematch(pod, previous_pods):
    for previous_pod in previous_pods:
        if set(pod).issubset(set(previous_pod)):
            return True
    return False

# Create Swiss-style pods, avoiding rematches
def swiss_pairings(players, pod_sizes, previous_pods, scores):
    sorted_players = sort_players(players, scores, previous_pods)
    pods = []
    start = 0
    
    for size in pod_sizes:
        pod = sorted_players[start:start + size]
        
        # Adjust if a rematch is detected
        while is_rematch(pod, previous_pods):
            pod = pod[1:] + [pod[0]]  # Simple rotation to avoid rematch

        pods.append(pod)
        start += size
    
    return pods

# Main function to run the tournament
def run_tournament():
    players = get_player_names()
    scores = {player: 0 for player in players}
    previous_pods = []
    
    # Round 1
    pods = create_initial_pods(players)
    previous_pods.extend(pods)
    print("Round 1 Pods:", pods)

    # Simulate results entry manually for testing
    results = [input(f"Enter result order for Pod {i + 1} separated by commas: ").split(",") for i in range(len(pods))]

    scores = update_scores(pods, results, scores)
    print("Scores after Round 1:", scores)

    # Round 2 - Swiss pairings
    pod_sizes = determine_pod_sizes(len(players))
    pods = swiss_pairings(players, pod_sizes, previous_pods, scores)
    previous_pods.extend(pods)
    print("Round 2 Pods:", pods)

    # Simulate results entry again
    results = [input(f"Enter result order for Pod {i + 1} separated by commas: ").split(",") for i in range(len(pods))]

    scores = update_scores(pods, results, scores)
    print("Scores after Round 2:", scores)

    # Round 3 - Final Swiss pairings
    pods = swiss_pairings(players, pod_sizes, previous_pods, scores)
    previous_pods.extend(pods)
    print("Round 3 Pods:", pods)

    # Simulate results entry for Round 3
    results = [input(f"Enter result order for Pod {i + 1} separated by commas: ").split(",") for i in range(len(pods))]

    scores = update_scores(pods, results, scores)

    # Sort final scores in descending order
    sorted_final_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print("Final Scores:", sorted_final_scores)

# Run the tournament
run_tournament()