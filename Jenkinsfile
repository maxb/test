pipeline {
    agent any

    stages {
        stage('Stage One') {
            steps {
                // sh 'git checkout -B "$GIT_BRANCH"'
                sh 'date >> datefile.txt'
                sh 'git add datefile.txt'
                sh 'git commit -m "Automatic commit from Jenkins"'
                withCredentials([usernamePassword(credentialsId: 'maxb-github-app',
                                                  usernameVariable: 'GITHUB_APP',
                                                  passwordVariable: 'GITHUB_ACCESS_TOKEN')]) {
                    sh 'git push https://$GITHUB_APP:$GITHUB_ACCESS_TOKEN@github.com/maxb/test'
                }
            }
        }
    }

    post {
        success {
            echo 'Good'
        }
        unsuccessful {
            echo 'Bad'
        }
    }
}

// vim:sw=4:et
