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
        sh 'python --version'
      }
    }
    stage('sort') {
      steps {
        sh 'python pallindrome.py'
      }
    }
    
  }
}
