pipeline {
    agent any

    stages {
        stage('Template Formatting') {
            when { not { branch 'master' } }
            steps {
                // sh 'git checkout -B "$GIT_BRANCH"'
                sh './format-template.py'
                withCredentials([usernamePassword(credentialsId: 'maxb-github-app',
                                                  usernameVariable: 'GITHUB_APP',
                                                  passwordVariable: 'GITHUB_ACCESS_TOKEN')]) {
                    sh '''
                    git add -A .
                    if [ "$(git status --porcelain)" ]; then
                        git commit -m "Automatic commit from Jenkins"
                        git push https://$GITHUB_APP:$GITHUB_ACCESS_TOKEN@github.com/maxb/test
                    fi
                    '''
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
