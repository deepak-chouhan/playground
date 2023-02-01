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
    
//     stage('version') {
//       steps {
//         sh 'python3 --version'
//       }
//     }
    stage('sort') {
      steps {
        sh 'python pallindrome.py'
      }
    }
    
  }
}
