pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('sort') {
      steps {
        sh 'python bubbleSort.py '
      }
    }
  }
}
