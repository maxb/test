if (true) {
  echo 'This build will use legacySCM same branch technique'
  library(identifier: 'this-repo@current-branch', retriever: legacySCM(scm))
} else {
  echo 'This build will use modernSCM SPECIFIED branch technique'
  library(identifier: 'this-repo@master',
          retriever: modernSCM([$class: 'GitSCMSource',
                                remote: scm.userRemoteConfigs[0].url,
                                credentialsId: scm.userRemoteConfigs[0].credentialsId]))
}

pipeline {
  agent any

  parameters {
    booleanParam(name: 'BOOLEAN')
    script {
      log.info 'Params'
    }
  }

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
