def calculate_response_accuracy(correct_responses, total_queries):
    return (correct_responses / total_queries) * 100

def calculate_response_time(total_response_time, total_queries):
    return total_response_time / total_queries

def calculate_api_success_rate(successful_calls, total_calls):
    return (successful_calls / total_calls) * 100

def test_context_retention(test_cases):
    # Example function for testing context retention
    correct_context_cases = sum([1 for case in test_cases if case['context_retained']])
    return (correct_context_cases / len(test_cases)) * 100
