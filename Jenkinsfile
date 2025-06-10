pipeline {
    agent any

    environment {
        API_URL = credentials('API_URL')
        UNSPLASH_ACCESS_KEY = credentials('UNSPLASH_ACCESS_KEY')
        API_PHOTOS = credentials('API_PHOTOS')
        API_COLLECTIONS = credentials('API_COLLECTIONS')
        API_USERS = credentials('API_USERS')
        API_SEARCH = credentials('API_SEARCH')
        API_TOPICS = credentials('API_TOPICS')
        TEST_PHOTO_ID = credentials('TEST_PHOTO_ID')
        TEST_COLLECTION_ID = credentials('TEST_COLLECTION_ID')
        TEST_USER_USERNAME = credentials('TEST_USER_USERNAME')
        TEST_TOPIC_ID_OR_SLUG = credentials('TEST_TOPIC_ID_OR_SLUG')
        TEST_SEARCH_QUERY = credentials('TEST_SEARCH_QUERY')
        // You can configure these Secret Text credentials in the Jenkins management interface
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                sh 'sudo apt-get update && sudo apt-get install -y default-jre-headless'
            }
        }
        stage('Install Allure CLI') {
            steps {
                sh '''
                    ALLURE_VERSION="2.34.0"
                    DEB_PACKAGE="allure_${ALLURE_VERSION}-1_all.deb"
                    wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/${DEB_PACKAGE}
                    sudo dpkg -i ${DEB_PACKAGE}
                    rm ${DEB_PACKAGE}
                '''
                sh 'allure --version'
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'chmod +x run-pytest.sh'
                sh '. .venv/bin/activate && ./run-pytest.sh'
            }
        }
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'test-reports/**/*', allowEmptyArchive: true
                junit 'test-reports/**/*.xml'
                // Publish pytest-html report (requires HTML Publisher Plugin)
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'test-reports',
                    reportFiles: 'report-*.html',
                    reportName: 'Pytest HTML Report',
                    reportTitles: 'Pytest HTML Report'
                ])
                // Publish pytest-cov HTML report (requires HTML Publisher Plugin)
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'test-reports/pytest-cov',
                    reportFiles: 'cov-*-html/index.html',
                    reportName: 'Coverage Report',
                    reportTitles: 'Coverage Report'
                ])
            }
        }
    }
    post {
        always {
            // Optional: Publish Allure report (requires Allure Jenkins Plugin)
            allure includeProperties: false, jdk: '', results: [[path: 'test-reports/allure/results']]
        }
    }
}