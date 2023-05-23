pipeline {
 agent {
    docker { image 'python:3.9-bullseye' }
 }
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
        sh 'python3 pallindrome.py'
      }
    }
    
  }
}
