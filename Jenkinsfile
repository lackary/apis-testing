pipeline {
    agent {
        docker {
            image 'python:3.13'
        }
    }

    environment {
        UNSPLASH_ACCESS_KEY = credentials('UNSPLASH_ACCESS_KEY')
        // You can configure these Secret Text credentials in the Jenkins management interface
    }

    stages {
        stage('Clean Reports') {
            steps {
                sh 'rm -rf test-reports/*'
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Check Python') {
            steps {
                sh 'python --version'
            }
        }
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Setup Java') {
            steps {
                sh 'apt-get update && apt-get install -y default-jre-headless'
            }
        }
        stage('Install Allure CLI') {
            steps {
                sh '''
                    ALLURE_VERSION="2.34.0"
                    DEB_PACKAGE="allure_${ALLURE_VERSION}-1_all.deb"
                    wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/${DEB_PACKAGE}
                    dpkg -i ${DEB_PACKAGE}
                    rm ${DEB_PACKAGE}
                '''
                sh 'allure --version'
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'chmod +x run-pytest.sh'
                script {
                    // Execute the script, logs will be displayed in the Console
                    def runOutput = sh(
                        script: '. .venv/bin/activate && ./run-pytest.sh',
                        returnStdout: true
                    ).trim()
                    // Display all output to Console
                    echo runOutput
                    // Get the last line as RUN_ID
                    def lines = runOutput.readLines()
                    env.RUN_ID = lines[-1]
                }
                echo "Pytest run ID: ${env.RUN_ID}"
            }
        }
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'test-reports/**/*', allowEmptyArchive: true
            }
        }
    }
    post {
        always {
            script {
                // Publish JUnit test report
                def pytestJUnitReportDir = "test-reports"
                def pytestJUnitReportFile = "test-${env.RUN_ID}.xml"
                echo "Publishing Pytest JUnit report from: ${pytestJUnitReportDir}/${pytestJUnitReportFile}"
                if (fileExists("${pytestJUnitReportDir}/${pytestJUnitReportFile}")) {
                    junit "${pytestJUnitReportDir}/${pytestJUnitReportFile}"
                    echo "✅ JUnit report published"
                } else {
                    echo "❌ No JUnit XML found"
                }
                // --- Publish Pytest HTML Report ---
                def pytestHtmlReportDir = "test-reports"
                def pytestHtmlReportFile = "report-${env.RUN_ID}.html"
                echo "Publishing Pytest HTML report from: ${pytestHtmlReportDir}/${pytestHtmlReportFile}"
                // Check if the pytest HTML report file exists
                if (fileExists("${pytestHtmlReportDir}/${pytestHtmlReportFile}")) {
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: false,
                        reportDir: pytestHtmlReportDir,
                        reportFiles: pytestHtmlReportFile,
                        reportName: 'Pytest HTML Report',
                        reportTitles: 'Pytest HTML Report'
                    ])
                    echo "✅ Successfully published Pytest HTML report: ${pytestHtmlReportFile}"
                } else {
                    echo "❌ Pytest HTML report file '${pytestHtmlReportFile}' not found in '${pytestHtmlReportDir}'. Skipping publishing."
                    // currentBuild.result = 'FAILURE'
                }

                // --- Publish Pytest-Cov HTML Report ---
                def pytestCovHtmlReportBaseDir = "test-reports/pytest-cov"
                def pytestCovHtmlReportRelativeDir = "cov-${env.RUN_ID}-html"
                def fullPytestCovHtmlReportDir = "${pytestCovHtmlReportBaseDir}/${pytestCovHtmlReportRelativeDir}"
                echo "Publishing Pytest-Cov HTML report from: ${fullPytestCovHtmlReportDir}"

                // Check if the pytest-cov report directory exists
                if (fileExists(fullPytestCovHtmlReportDir)) {
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: false,
                        reportDir: fullPytestCovHtmlReportDir, // Note: This points directly to the directory containing index.html
                        reportFiles: 'index.html', // Pytest-Cov HTML report main entry file is usually index.html
                        reportName: 'Pytest Coverage Report',
                        reportTitles: 'Pytest Coverage Report'
                    ])
                    echo "✅ Successfully published Pytest Coverage Report from: ${fullPytestCovHtmlReportDir}"
                } else {
                    echo "❌ Pytest Coverage report directory '${fullPytestCovHtmlReportDir}' not found. Skipping publishing."
                }

                // --- Publish Allure Report ---
                def allureResultsPath = "test-reports/allure/results/results-${env.RUN_ID}"
                echo "Publishing Allure Report from results in: ${allureResultsPath}"

                // Check if the Allure results directory exists
                if (fileExists(allureResultsPath)) {
                    allure([
                        allureCommandline: 'Allure', // Make sure this matches the Allure Commandline name in Jenkins global tool configuration
                        reportBuildExitCode: 0,
                        results: [[path: allureResultsPath]]
                    ])
                    echo "✅ Successfully published Allure Report from results in: ${allureResultsPath}"
                } else {
                    echo "❌ Allure results directory '${allureResultsPath}' not found. Skipping Allure Report publishing."
                }
            }
        }
        success {
            echo "Pipeline completed successfully."
        }
        failure {
            echo "Pipeline failed. Please check the logs for details."
        }
        unstable {
            echo "Pipeline completed with unstable status."
        }
        changed {
            echo "Pipeline status has changed."
        }
        aborted {
            echo "Pipeline was aborted."
        }
        cleanup {
            echo "Cleaning up resources..."
            // You can add any cleanup steps here if needed
            cleanWs() // Clean workspace after the build
        }
    }
}