pipeline {
  agent {
      docker {
        image 'python:3'
        label 'my-build-agent'
      }
  }
  stages {
    stage('hello') {
      steps {
        echo "Hello World!"
      }
    }
  }
}
