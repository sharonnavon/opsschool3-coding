node ('aws_dyn_slave'){
  echo 'Strating weather script:'

    stages{
      stage('---clean---'){
        steps{
            sh "mvn clean"
        }
      }
      stage('---test---'){
        steps{
            sh "mvn test"
        }
      }
      stage('---package---'){
        steps{
            dir('dir3') {
               git url: 'https://github.com/sharonnavon/opsschool3-coding.git'
           }
        }
      }
      sh '''
            #!/bin/bash
            ls -l
            pwd
         '''
    }
}
