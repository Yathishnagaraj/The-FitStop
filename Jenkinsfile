pipeline {
    agent any

    environment {
        IMAGE_NAME = "yathish047/thefitstop"
        IMAGE_TAG  = "latest"
        CONTAINER_NAME = "thefitstop-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Yathishnagaraj/The-FitStop.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    docker logout
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                sh """
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                docker pull ${IMAGE_NAME}:${IMAGE_TAG}
                docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }
    }
}
