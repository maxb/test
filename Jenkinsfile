library(
  identifier: 'vvp@master',
  retriever: modernSCM([
    $class: 'GitSCMSource',
    remote: 'https://github.com/maxb/test'
  ])
)

def testStep(String name) {
  sh "echo 'Now we are testing ${name}'"
}

pipeline {
  agent any

  options {
    skipDefaultCheckout()
  }

  stages {
    stage('Do something')      { steps { script { testStep('something') }}}
    stage('Do something else') { steps { script { testStep('something else') }}}

    stage('Use library') {
      steps {
        common foo: 1 {
        }
      }
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
