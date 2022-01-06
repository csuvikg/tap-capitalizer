pipeline {
    agent { node { label 'docker' } }

    // checkout code from GitHub

    stages {
        stage('Build app') {
            steps {
                // Create venv
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                // Install dependencies
                sh 'pip3 install -r requirements.txt'
            }
        }

//         stage('Lint code') {
//             steps {
//                 // Lint
//                 sh 'pylint app.py'
//             }
//         }

        stage('Run sonarqube') {
            steps {
                // Run sonarqube
                withCredentials([string(credentialsId: 'capitalizer-sonarqube', variable: 'SONARQUBE_TOKEN')]) {
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
                sh 'py.test --junitxml results.xml test.py'
                junit 'results.xml'
            }
        }
    }

//     post {
//         always {
// //             deleteDir()
//         }
//     }
}
