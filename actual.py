import requests
from collections import defaultdict

# Fetch JSON data
surveys = requests.get("https://interview-data-mock-api.s3.us-west-2.amazonaws.com/surveys.json").json()
questions = requests.get("https://interview-data-mock-api.s3.us-west-2.amazonaws.com/survey_questions.json").json()
responses = requests.get("https://interview-data-mock-api.s3.us-west-2.amazonaws.com/survey_responses.json").json()

# Step 1: Build lookup dictionaries
survey_lookup = {survey["id"]: survey["name"] for survey in surveys}
question_lookup = {question["id"]: (question["survey_id"], question["prompt"]) for question in questions}

# Step 2: Aggregate scores
survey_data = defaultdict(list)

for response in responses:
    question_id = response["question_id"]
    score = response["score"]
    survey_id, prompt = question_lookup.get(question_id, (None, None))
    if survey_id and prompt:
        survey_data[(survey_id, prompt)].append(score)

# Step 3: Calculate and print averages
for (survey_id, prompt), scores in survey_data.items():
    survey_name = survey_lookup.get(survey_id, "Unknown Survey")
    average_score = sum(scores) / len(scores) if scores else 0
    print(f"{survey_name}\n{'_' * 6}\n{prompt}\nAverage score: {average_score:.2f}\n")
