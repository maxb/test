pipeline {
    agent any

    stages {
        stage('Stage One') {
            steps {
                sh 'git checkout "$GIT_BRANCH"'
                sh 'date >> datefile.txt'
                sh 'git add datefile.txt'
                sh 'git commit -m "Automatic commit from Jenkins"'
                sh 'git push'
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
