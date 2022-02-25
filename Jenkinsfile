if (currentBuild.number % 3 == 0) {
  echo 'This build will use legacySCM same branch technique'
  library(identifier: 'this-repo@current-branch', retriever: legacySCM(scm))
} else if (currentBuild.number % 3 == 1) {
  echo 'This build will use modernSCM same branch technique'
  library(identifier: 'this-repo@current-branch',
          retriever: modernSCM(fromScm(name: 'current-branch', scm: scm)))
} else {
  echo 'This build will use modernSCM SPECIFIED branch technique'
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
