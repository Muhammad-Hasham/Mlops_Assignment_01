pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                // Build Docker image using Dockerfile
                bat 'docker build -t my-flask-app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                // Push Docker image to Docker registry (replace with your Docker registry details)
                bat 'docker login -u MuhammadHasham1 -p F4D00E8CC'
                bat 'docker tag my-flask-app MuhammadHasham1/my-flask-app:latest'
                bat 'docker push MuhammadHasham1/my-flask-app:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
