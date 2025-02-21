pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                    git credentialsId: 'cred-jenkins', 
                    url: 'https://github.com/CHINNAKOTLAJAGANNATH/Capstone_Project_API.git',
                    branch: 'main'
            }
        }
    }
}
