def demoStage(String name, Closure body) {
  stage(name) {
    steps {
      body()
    }
  }
}

pipeline {
  agent any

  options {
    skipDefaultCheckout()
  }

  stages {
    demoStage('Do something') {
      sh "echo Something!"
    }

    stage('Template Formatting') {
      when { not { branch 'master' } }
      steps {
        checkout scm

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

// vim:sw=2:et
