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
pytest -v \
  --html=reports/pytest-html/report-${RUN_ID}.html \
  --self-contained-html \
  --alluredir=reports/allure/results-${RUN_ID}

# Generate Allure HTML report
allure generate reports/allure/results-${RUN_ID} -o reports/allure/report-${RUN_ID} --clean

# Check if pytest and allure commands were successful
if [[ $? -ne 0 ]]; then
  echo "❌ Tests failed or reports could not be generated."
  exit 1
fi

# Print success message
echo "✅ Tests completed successfully and reports generated."

# Check if the reports directory exists
if [[ ! -d "reports/pytest-html" ]] || [[ ! -d "reports/allure/results-${RUN_ID}" ]]; then
  echo "❌ Reports directory does not exist."
  exit 1
fi

# Check if the generated reports exist
if [[ ! -f "reports/pytest-html/report-${RUN_ID}.html" ]] || [[ ! -d "reports/allure/report-${RUN_ID}" ]]; then
  echo "❌ Generated reports do not exist."
  exit 1
fi

# Print the success message
echo "✅ All reports generated successfully."

# Print the location of the generated reports
echo "✅ Pytest-HTML: reports/pytest-html/report-${RUN_ID}.html"
echo "✅ Allure HTML: reports/allure/report-${RUN_ID}"

# Print the run ID for reference
echo "Run ID: ${RUN_ID}"

# Optionally, you can open the generated HTML report in a web browser
allure open reports/allure/report-${RUN_ID}

# Uncomment the following line to open the report automatically
# xdg-open reports/pytest-html/report-${RUN_ID}.html || open reports/pytest-html/report-${RUN_ID}.html

# Exit with success status
exit 0
