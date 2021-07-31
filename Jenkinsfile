pipeline {
    agent any

    stages {
        stage('Template Formatting') {
            when { not { branch 'master' } }
            steps {
                // sh 'git checkout -B "$GIT_BRANCH"'
                sh './format-template.py'
                sh 'git add -A .'
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
