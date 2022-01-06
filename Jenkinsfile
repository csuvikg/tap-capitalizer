pipeline {
    agent { node { label 'docker' } }

    parameters {
        string(name: 'SONARQUBE_CREDENTIALS_ID', defaultValue: 'capitalizer-sonarqube')
    }

    parameters {
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
                sh "docker build . --tag tap-capitalizer:${params.DOCKER_TAG}"
            }

        }
        // push to docker registry (Docker Hub)
        // connect to cluster
        // deploy to K8S
    }

    post {
        always {
            deleteDir()
        }
    }
}
