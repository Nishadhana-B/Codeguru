import time
import boto3

# Initialize the CodeGuru Reviewer client
client = boto3.client('codeguru-reviewer', region_name='us-east-1')

# Function to check the status of a code review
def check_code_review_status(code_review_arn):
    while True:
        response = client.describe_code_review(CodeReviewArn=code_review_arn)
        status = response['CodeReview']['State']
        print(f"Code review status: {status}")
        if status in ['Completed', 'Failed']:
            break
        time.sleep(30)  # Wait for 30 seconds before checking again

    return response

# Replace with the ARN of the code review created in Step 3
code_review_arn = 'arn:aws:codeguru-reviewer:us-east-1:123456789012:code-review-id'
review_response = check_code_review_status(code_review_arn)
print("Code review result:", review_response)
\
    