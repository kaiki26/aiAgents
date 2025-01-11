def calculate_skill_synchronization(coordinated_actions, total_actions):
    return (coordinated_actions / total_actions) * 100

def calculate_strategic_contribution(game_metrics):
    return sum(game_metrics) / len(game_metrics)

def calculate_error_rate(errors, total_actions):
    return (errors / total_actions) * 100

def calculate_player_trust_score(trust_feedback):
    return sum(trust_feedback) / len(trust_feedback)

def calculate_engagement_score(feedback_scores):
    return sum(feedback_scores) / len(feedback_scores)
