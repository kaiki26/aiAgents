def calculate_state_reading_accuracy(correct_readings, total_readings):
    return (correct_readings / total_readings) * 100

def calculate_latency(commentary_time, event_time):
    return commentary_time - event_time

def calculate_engagement_score(feedback_scores):
    return sum(feedback_scores) / len(feedback_scores)

def evaluate_relevance(test_cases):
    relevance_scores = [case['relevance_score'] for case in test_cases]
    return sum(relevance_scores) / len(relevance_scores)
