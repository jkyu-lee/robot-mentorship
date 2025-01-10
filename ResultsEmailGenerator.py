from robot.api import ExecutionResult

# Load the execution result from the output.xml file
result = ExecutionResult('results/output.xml')

# Extract statistics
statistics = result.statistics
summary = []

# Iterate over suites and tests to gather summary information
for suite in statistics.suites:
    suite_summary = f"Suite: {suite.name}\n"
    suite_summary += f"Tests Passed: {suite.passed}\n"
    suite_summary += f"Tests Failed: {suite.failed}\n"
    suite_summary += f"Tests Total: {suite.total}\n"
    summary.append(suite_summary)

# Combine all summaries into one string
test_summary = "\n".join(summary)

# Print the test summary
print(test_summary)