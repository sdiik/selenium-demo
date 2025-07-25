pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --html=report.html'
            }
        }
        stage('Publish HTML Report') {
            steps {
                publishHTML (target : [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: "Test Report"
                ])
            }
        }
    }
}