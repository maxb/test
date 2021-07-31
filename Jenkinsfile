pipeline {
    agent any

    stages {
        stage('Stage One') {
            steps {
                echo 'Hello World!'
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
