#!/bin/bash

# Enable debug mode (optional: print each executed command)
# set -x

# Exit immediately if any command fails
# set -e

# Set a timestamp-based run ID for naming the reports
RUN_ID=$(date +"%Y%m%d_%H%M%S")

# # (Optional) Remove old report directory
# rm -rf reports/

# # Create directory structure for reports
# mkdir -p reports/pytest-html
# mkdir -p reports/allure/results

# Run tests and generate both pytest-html and Allure result files
pytest \
  --html=test-reports/report-${RUN_ID}.html \
  --self-contained-html \
  --alluredir=test-reports/allure/results/results-${RUN_ID} \
  --cov=src \
  --cov-report=term-missing \
  --cov-report=html:test-reports/pytest-cov/cov-${RUN_ID}-html \
  --log-file=test-reports/logs/test-${RUN_ID}.log

# Detect OS for sed -i compatibility
if [[ "$OSTYPE" == "darwin"* ]]; then
  SED_ARGS=(-i '' -E)
else
  SED_ARGS=(-i -E)
fi

sed "${SED_ARGS[@]}" 's/([0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3})[0-9]{3}/\1/' test-reports/logs/test-${RUN_ID}.log

# # Mask Client-ID <key> in headers
sed "${SED_ARGS[@]}" 's/(Client-ID )[a-zA-Z0-9_-]+/\1****/g' test-reports/logs/test-${RUN_ID}.log

# # Mask Authorization header
sed "${SED_ARGS[@]}" 's/(Authorization: ?)[a-zA-Z0-9_-]+/\1****/g' test-reports/logs/test-${RUN_ID}.log

# Mask Authorization=Client-ID+<key> in URL
sed "${SED_ARGS[@]}" 's/(Authorization=Client-ID\+)[a-zA-Z0-9_-]+/\1****/g' test-reports/logs/test-${RUN_ID}.log

# Generate Allure HTML report
allure \
  generate test-reports/allure/results/results-${RUN_ID} \
  -o test-reports/allure/reports/report-${RUN_ID} \
  --clean

# Check if pytest and allure commands were successful
if [[ $? -ne 0 ]]; then
  echo "❌ Tests failed or reports could not be generated."
  exit 1
fi

# Print success message
echo "✅ Tests completed successfully and reports generated."

# Check if the reports directory exists
if [[ ! -d "test-reports" ]] || [[ ! -d "test-reports/allure/results/results-${RUN_ID}" ]]; then
  echo "❌ Reports directory does not exist."
  exit 1
fi

# Check if the generated reports exist
if [[ ! -f "test-reports/report-${RUN_ID}.html" ]] || [[ ! -d "test-reports/allure/reports/report-${RUN_ID}" ]]; then
  echo "❌ Generated reports do not exist."
  exit 1
fi

# Print the success message
echo "✅ All reports generated successfully."

# Print the location of the generated reports
echo "✅ Pytest-HTML: test-reports/report-${RUN_ID}.html"
echo "✅ Allure HTML: test-reports/allure/reports/report-${RUN_ID}"
echo "✅ Coverage HTML: test-reports/pytest-cov/cov-${RUN_ID}-html"

# Print the run ID for reference
echo "Run ID: ${RUN_ID}"

# Optionally, you can open the generated HTML report in a web browser
# allure open test-reports/allure/reports/report-${RUN_ID}
# open test-reports/pytest-cov/cov-${RUN_ID}-html/index.html
# open test-reports/report-${RUN_ID}.html

# Uncomment the following line to open the report automatically
# xdg-open test-reports/report-${RUN_ID}.html || test-reports/report-${RUN_ID}.html
# xdg-open test-reports/allure/reports/report-${RUN_ID} || test-reports/allure/reports/report-${RUN_ID}
# xdg-open test-reports/pytest-cov/cov-${RUN_ID}-html/index.html || test-reports/pytest-cov/cov-${RUN_ID}-html/index.html

# Exit with success status
exit 0
