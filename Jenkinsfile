pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-v /var/run/docker.sock:/var/run/docker.sock -v $WORKSPACE:/app -w /app'
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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                // pastikan plugin Allure diinstall di Jenkins dan konfigurasi commandline-nya benar
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/allure-results/*.json', allowEmptyArchive: true
            junit 'tests/**/results.xml'
        }
        failure {
            echo "Build failed. Please check the test report and logs."
        }
    }
}