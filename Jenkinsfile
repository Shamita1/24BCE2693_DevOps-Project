pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')   // Jenkins credential ID (username+password)
        IMAGE_NAME             = "shamitar/abc-technologies-website"
        IMAGE_TAG               = "${env.BUILD_NUMBER}"
        KUBECONFIG_CRED         = credentials('kubeconfig-file')  // Jenkins "Secret file" credential (optional)
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

        stage('Deploy to Kubernetes') {
    steps {
        echo 'Deploying to Kubernetes cluster...'
        sh '''
            sed -i "s|__IMAGE__|$IMAGE_NAME:$IMAGE_TAG|g" k8s/deployment.yaml
            kubectl apply -f k8s/deployment.yaml --validate=false
            kubectl apply -f k8s/service.yaml --validate=false
            kubectl rollout status deployment/abc-website-deployment
        '''
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
