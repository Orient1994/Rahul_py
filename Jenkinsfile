pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sleep(time: 2, unit: 'SECONDS')
        echo 'executing print msg'
        sh 'echo  "Installing NPM for nodejs"'
      }
    }

  }
  environment {
    task = 'demo'
    tag = '0.9'
  }
}