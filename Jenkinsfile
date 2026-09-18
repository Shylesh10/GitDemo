pipeline {
    agent any

    environment {
        // Set Python path if needed for your Jenkins agent
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {

        stage('Checkout') {
            steps {
                // Pull the latest code from GitHub
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('saucedemo_playwright') {
                    sh '''
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                dir('saucedemo_playwright') {
                    sh 'playwright install chromium --with-deps'
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('saucedemo_playwright') {
                    // Run in headless mode for CI (no display available)
                    sh '''
                        python -m pytest tests/test_saucedemo_e2e.py \
                            -v \
                            --headless \
                            --html=reports/report.html \
                            --self-contained-html
                    '''
                }
            }
        }
    }

    post {
        always {
            // Archive the HTML report so it is accessible from Jenkins UI
            archiveArtifacts artifacts: 'saucedemo_playwright/reports/report.html',
                             allowEmptyArchive: true

            // Publish the HTML report in the Jenkins job sidebar
            publishHTML(target: [
                allowMissing         : false,
                alwaysLinkToLastBuild: true,
                keepAll              : true,
                reportDir            : 'saucedemo_playwright/reports',
                reportFiles          : 'report.html',
                reportName           : 'Playwright Test Report'
            ])
        }

        success {
            echo '✅ All tests passed!'
        }

        failure {
            echo '❌ One or more tests failed. Check the HTML report above.'
        }
    }
}

