pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scmGit(
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/CHINNAKOTLAJAGANNATH/Capstone_Project_API.git',
                        credentialsId: 'cred-jenkins'
                    ]]
                )
            }
        }
        
        stage('Set Up Python Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pytest tests/'
                    } else {
                        bat 'pytest tests/'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Build Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}
