pipeline {
    agent any

    environment {
        IMAGE_NAME = 'calculator-app'
        CONTAINER_NAME = 'calculator-container'
    }

    stages {
        stage('Code checkout') {
            steps {
                git branch: 'main',
                    changelog: false, 
                    credentialsId: 'e13c68cb-01e8-45eb-bfd4-1541c3d55ca5', 
                    poll: false, 
                    url: 'https://github.com/aditingale-hash/calculator.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }
stage('Run Unit Tests') {
    steps {
        bat """
        call venv\\Scripts\\activate
        pip install pytest
        pytest tests/ || exit /b 1
        """
    }
}

        stage('Lint Code') {
            steps {
                bat """
                call venv\\Scripts\\activate
                pip install pylint
                pylint calculator.py || exit /b 0
                """
            }
        }
        
       stage('Security Scan (Bandit)') {
    steps {
        bat """
        call venv\\Scripts\\activate
        pip install bandit
        call venv\\Scripts\\python.exe -m bandit -r . -ll -f html -o bandit_report.html || exit /b 0
        dir bandit_report.html
        """
    }
}



        stage('Build Docker Image') {
            steps {
                bat 'echo Building image %IMAGE_NAME%'
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Stop Existing Container') {
            steps {
                bat 'docker rm -f %CONTAINER_NAME% || exit /b 0'
            }
        }

        stage('Run New Container') {
            steps {
                bat 'echo Running container %CONTAINER_NAME% from image %IMAGE_NAME%'
                bat 'docker run -d --name %CONTAINER_NAME% -p 8501:8501 %IMAGE_NAME%'
            }
        }
    }

   post {
    always {
        archiveArtifacts artifacts: 'bandit_report.html', onlyIfSuccessful: false
    }
    success {
        echo '✅ Deployed successfully! Visit http://localhost:8501'
    }
    failure {
        echo '❌ Build failed! Check the logs.'
    }
}
}

