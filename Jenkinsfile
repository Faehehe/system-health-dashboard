pipeline {
    agent any

    environment {
        IMAGE_NAME = 'system-health-dashboard'
        APP_ENVIRONMENT = 'production'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ."
            }
        }

        stage('Tag') {
            steps {
                bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
            }
        }

        stage('Health Check') {
            steps {
                bat """
                    docker run -d -p 5000:5000 -e APP_ENVIRONMENT=%APP_ENVIRONMENT% --name shd-%BUILD_NUMBER% %IMAGE_NAME%:%BUILD_NUMBER%
                    timeout /t 5 /nobreak
                    curl -f http://localhost:5000/health
                """
            }
        }
    }

    post {
        always {
            bat "docker stop shd-%BUILD_NUMBER% || exit 0"
            bat "docker rm shd-%BUILD_NUMBER% || exit 0"
        }
    }
}