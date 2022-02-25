// Either of these work
if (currentBuild.number % 2 == 0) {
  library(identifier: 'this-repo@current-branch', retriever: legacySCM(scm))
} else {
  library(identifier: 'this-repo@current-branch',
          retriever: modernSCM(fromScm(name: 'current-branch', scm: scm)))
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
