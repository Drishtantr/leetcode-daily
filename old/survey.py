import pandas as pd

def analyze_survey(data):
    # Load the data
    df = pd.DataFrame(data)
    
    # Basic cleaning: Drop missing values
    df = df.dropna()
    
    # Aggregate engagement scores by department
    engagement_scores = df.groupby('department')['engagement_score'].mean().to_dict()

    print(engagement_scores)

    # Identify department with highest and lowest engagement
    highest_engagement = max(engagement_scores, key=engagement_scores.get)
    lowest_engagement = min(engagement_scores, key=engagement_scores.get)
    
    return {
        "engagement_scores": engagement_scores,
        "highest_engagement": highest_engagement,
        "lowest_engagement": lowest_engagement
    }

# Example usage
survey_data = [
    {"employee_id": 1, "department": "HR", "engagement_score": 8},
    {"employee_id": 2, "department": "Engineering", "engagement_score": 7},
    {"employee_id": 3, "department": "HR", "engagement_score": 6},
    {"employee_id": 4, "department": "Engineering", "engagement_score": 9}
]
print(analyze_survey(survey_data))
