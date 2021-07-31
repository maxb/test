pipeline {
    agent any

    stages {
        stage('Template Formatting') {
            when { not { branch 'master' } }
            steps {
                // Only needed if you can't configure the "Check out to matching local branch" behaviour:
                // sh 'git checkout -B "$GIT_BRANCH"'

                sh './format-template.py'

                script {
                    def gitStatus = sh script: 'git status --porcelain', returnStdout: true
                    if (gitStatus != "") {
                        withCredentials([usernamePassword(credentialsId: 'maxb-github-app',
                                                          usernameVariable: 'GITHUB_APP',
                                                          passwordVariable: 'GITHUB_ACCESS_TOKEN')]) {
                            sh '''
                                git add -A .
                                git commit -m "Automatic commit from Jenkins"
                                git push https://$GITHUB_APP:$GITHUB_ACCESS_TOKEN@github.com/maxb/test
                            '''
                            unstable 'Template formatting has modified the branch'
                        }
                    }
                }
            }
        }
    }
}

// vim:sw=4:et
