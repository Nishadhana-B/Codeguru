import boto3

# Initialize the CodeGuru Reviewer client
client = boto3.client('codeguru-reviewer', region_name='us-east-1')

# Function to get recommendations
def get_findings(code_review_arn):
    findings = client.list_recommendations(CodeReviewArn=code_review_arn)
    for finding in findings['RecommendationSummaries']:
        print(f"File: {finding['FilePath']}")
        print(f"Description: {finding['Description']}")
        print(f"Severity: {finding['Severity']}")
        print('-' * 40)

# Replace with the ARN of the code review created in Step 3
code_review_arn = 'arn:aws:codeguru-reviewer:us-east-1:123456789012:code-review-id'
get_findings(code_review_arn)
