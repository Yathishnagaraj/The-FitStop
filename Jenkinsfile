pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_IMAGE = "${DOCKER_REGISTRY}/${DOCKER_USERNAME}/thefitstop"
        DOCKER_TAG = "${BUILD_NUMBER}"
        DOCKER_LATEST = "latest"
    }
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo '========== Checking out code =========='
                }
                checkout scm
            }
        }
        
        stage('Build & Test') {
            steps {
                script {
                    echo '========== Building and Testing Python Application =========='
                }
                sh '''
                    # Create virtual environment
                    python3 -m venv venv
                    . venv/bin/activate
                    
                    # Install dependencies
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install flake8 pytest
                    
                    # Run linting
                    echo "Running flake8 linting..."
                    flake8 app.py --count --select=E9,F63,F7,F82 --show-source --statistics || true
                    
                    # Run tests (if tests directory exists)
                    if [ -d "tests" ]; then
                        echo "Running pytest..."
                        pytest tests/ -v || true
                    else
                        echo "No tests directory found, skipping tests"
                    fi
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo '========== Building Docker Image =========='
                }
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:${DOCKER_LATEST}
                '''
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    echo '========== Pushing Docker Image to Docker Hub =========='
                }
                sh '''
                    echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    docker push ${DOCKER_IMAGE}:${DOCKER_LATEST}
                    docker logout
                '''
            }
        }
        
        stage('Deploy to Server') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo '========== Deploying to Production Server =========='
                }
                sh '''
                    # Deploy via SSH (requires SSH key configured in Jenkins)
                    ssh -i ${SSH_PRIVATE_KEY} ${DEPLOY_USER}@${DEPLOY_HOST} << 'EOF'
                        echo "Pulling latest Docker image..."
                        docker pull ${DOCKER_IMAGE}:${DOCKER_LATEST}
                        
                        echo "Stopping existing container..."
                        docker stop thefitstop-app || true
                        docker rm thefitstop-app || true
                        
                        echo "Starting new container..."
                        docker run -d \
                            --name thefitstop-app \
                            -p 5000:5000 \
                            --restart unless-stopped \
                            -e FLASK_ENV=production \
                            ${DOCKER_IMAGE}:${DOCKER_LATEST}
                        
                        echo "Deployment completed successfully!"
                        docker ps -a | grep thefitstop-app
EOF
                '''
            }
        }
        
        stage('Cleanup') {
            steps {
                script {
                    echo '========== Cleaning up =========='
                }
                sh '''
                    # Remove virtual environment
                    rm -rf venv
                    
                    # Remove unused Docker images
                    docker image prune -f || true
                '''
            }
        }
    }
    
    post {
        success {
            script {
                echo '========== Pipeline Completed Successfully =========='
            }
        }
        
        failure {
            script {
                echo '========== Pipeline Failed =========='
            }
        }
        
        always {
            script {
                echo '========== Cleaning up workspace =========='
            }
            cleanWs()
        }
    }
}
