pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin"
    }

    stages {
        stage('Run Tests Inside Docker') {
            steps {
                sh '''
                docker pull python:3.10
                docker run --rm -v "$PWD":/app -w /app python:3.10 sh -c "
                  pip install -r requirements.txt &&
                  pytest tests/ --html=report.html
                "
                '''
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