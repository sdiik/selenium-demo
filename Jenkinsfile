pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir '.'
        }
    }

    environment {
        PYTHONPATH = "$WORKSPACE"
    }

    options {
        timestamps()
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install --no-cache-dir -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    pytest tests/ \
                        --alluredir=allure-results \
                        --junitxml=reports/junit-report.xml
                '''
            }
        }

        stage('Publish JUnit Report') {
            steps {
                junit 'reports/junit-report.xml'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: 'allure-results']],
                       commandline: 'allure'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/*.json', allowEmptyArchive: true
        }
        failure {
            echo "Build failed. Please check the test report and logs."
        }
    }
}