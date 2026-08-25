pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-task-manager .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat 'docker stop flask-task-manager-container || exit 0'
                bat 'docker rm flask-task-manager-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name flask-task-manager-container flask-task-manager'
            }
        }
    }

    post {

        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}