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
                script {
                    allure([
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
}
