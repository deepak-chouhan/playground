pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
        echo "Hello World!"
      }
    }
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('sort') {
      steps {
        sh 'python3 bubbleSort.py '
      }
    }
  }
}
