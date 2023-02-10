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
        bat 'python --version'
      }
    }
    stage('sort') {
      steps {
        bat 'python pallindrome.py'
      }
    }
    
  }
}
