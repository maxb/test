library(identifier: 'this-repo@this-repo', retriever: legacySCM(scm))

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
