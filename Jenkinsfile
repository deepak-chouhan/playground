pipeline {
  agent { docker { image 'python:3.10.7-alpine' } }
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 pallindrome.py'
      }
    }
  }
}
