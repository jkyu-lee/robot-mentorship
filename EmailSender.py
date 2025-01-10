import json
import boto3
from robot.api import ExecutionResult

def lambda_handler(event, context):
    # Load the test results from the output.xml file (assume it's passed to Lambda)
    result = ExecutionResult('/tmp/output.xml')  # Lambda temp storage

    # Extract statistics from output.xml
    statistics = result.statistics
    summary = []
    for suite in statistics.suites:
        suite_summary = f"Suite: {suite.name}\n"
        suite_summary += f"Tests Passed: {suite.passed}\n"
        suite_summary += f"Tests Failed: {suite.failed}\n"
        suite_summary += f"Tests Total: {suite.total}\n"
        summary.append(suite_summary)
    
    test_summary = "\n".join(summary)

    # SNS client setup
    sns_client = boto3.client('sns', region_name='us-west-2')

    # SNS Topic ARN (replace with your SNS topic ARN)
    sns_topic_arn = 'arn:aws:sns:us-west-2:039612886738:CodePipelineNotifications'

    # Publish the test summary to the SNS topic
    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=test_summary,
        Subject="Robot Framework Test Results"
    )

    # Return success response
    return {
        'statusCode': 200,
        'body': json.dumps('Test results sent via SNS!')
    }
