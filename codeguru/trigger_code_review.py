import boto3

# Initialize the CodeGuru Reviewer client
client = boto3.client('codeguru-reviewer', region_name='us-east-1')

# Trigger a repository analysis
response = client.create_code_review(
    Name='FullRepoAnalysis',
    RepositoryAssociationArn='arn:aws:codeguru-reviewer:us-east-1:123456789012:association-id',  # Replace with the ARN of your repository association
    Type={
        'RepositoryAnalysis': {
            'RepositoryHead': {
                'BranchName': 'main'  # Replace with your branch name
            }
        }
    }
)

print(f"Code review created: {response['CodeReview']['Name']}")
