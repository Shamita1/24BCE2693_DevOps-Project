pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')   // Jenkins credential ID (username+password)
        IMAGE_NAME             = "shamitar/abc-technologies-website"
        IMAGE_TAG               = "${env.BUILD_NUMBER}"
        
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository from GitHub...'
                git branch: 'main', url: 'https://github.com/Shamita1/24BCE2693_DevOps-Project.git'
            }
        }

        stage('Verify Website Files') {
            steps {
                echo 'Checking static site files exist...'
                sh 'ls -la src'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG -t $IMAGE_NAME:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
                sh 'docker push $IMAGE_NAME:latest'
            }
        }

        
    }

    post {
        success {
            echo 'Pipeline completed successfully! Website deployed.'
        }
        failure {
            echo 'Pipeline failed. Check console output above.'
        }
        always {
            sh 'docker logout || true'
        }
    }
}
