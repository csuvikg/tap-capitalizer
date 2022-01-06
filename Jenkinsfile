pipeline {
    agent { node { label 'docker' } }

    parameters {
        string(name: 'SONARQUBE_CREDENTIALS_ID', defaultValue: 'capitalizer-sonarqube')
        string(name: 'DOCKER_IMAGE', defaultValue: 'csuvikg/tap-capitalizer')
        string(name: 'DOCKER_TAG', defaultValue: 'latest')
    }

    // checkout code from GitHub

    stages {
        stage('Build app') {
            steps {
                // Create venv
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip3 install -r requirements.txt'
            }
        }

        stage('Lint code') {
            steps {
                // Lint
                sh '. venv/bin/activate && pylint app.py'
            }
        }

        stage('Run sonarqube') {
            steps {
                // Run sonarqube
                withCredentials([string(credentialsId: params.SONARQUBE_CREDENTIALS_ID, variable: 'SONARQUBE_TOKEN')]) {
                    sh '''sonar-scanner \
                          -Dsonar.projectKey=capitalizer \
                          -Dsonar.sources=. \
                          -Dsonar.host.url="$SONARQUBE_URL" \
                          -Dsonar.login="$SONARQUBE_TOKEN"'''
                }
            }
        }

        stage('Run tests') {
            steps {
                // Run tests
                sh '. venv/bin/activate && py.test --junitxml results.xml test.py'
                junit 'results.xml'
            }
        }

        stage('Build Docker image') {
            steps {
                // build docker image
                sh "docker build . --tag ${params.DOCKER_IMAGE}:${params.DOCKER_TAG}"
            }
        }

        stage('Push Docker image') {
            steps {
                withCredentials([
                    usernamePassword(credentialsId: 'dockerhub-csuvikg', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')
                ]) {
                    // push to docker registry (Docker Hub)
                    sh "docker login -u $USERNAME -p $PASSWORD"
                    sh "docker push ${params.DOCKER_IMAGE}:${params.DOCKER_TAG}"
                }
            }
        }
        // connect to cluster
        // deploy to K8S
    }

    post {
        always {
            deleteDir()
        }
    }
}
