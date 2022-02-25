println "Hello ${currentBuild.number}"
if (currentBuild.number % 2 == 0) {
  library(identifier: 'this-repo@current-branch', retriever: legacySCM(scm))
} else if (currentBuild.number % 2 == 1) {
  library(identifier: 'this-repo@current-branch',
          retriever: modernSCM(fromScm(name: 'current-branch', scm: scm)))
} else {
  library(identifier: 'this-repo@master',
          retriever: modernSCM([$class: 'GitSCMSource',
                                remote: scm.userRemoteConfigs[0].url,
                                credentialsId: 'maxb-github-app']))
}

pipeline {
  agent any

  stages {
    stage('Use library') {
      steps {
        script {
          log.info 'Starting'
          log.warning 'Nothing to do!'
        }
        hello 'world'
        wrapit {
          echo 'Body'
        }
      }
    }
  }
}

// vim:sw=2:et
