pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
        echo "Hello World!"
      }
    }

//     stage('Build') {
//       steps {
//           sh 'javac helloWorld.java'
//       }
//         }
//     stage('Run') {
//       steps {
//           sh 'java helloWorld'
//       }
//     }
    
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
