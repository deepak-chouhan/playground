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
        sh 'sudo apt-get update && apt-get install -y python3'
        sh 'python3 --version'
      }
    }
    stage('sort') {
      steps {
        sh 'python3 pallindrome.py'
      }
    }
    
  }
}
