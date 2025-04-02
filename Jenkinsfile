pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/example-user/calculator-streamlit-ci-cd.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('streamlit-calculator:latest', '.')
                }
            }
        }
    }
}
