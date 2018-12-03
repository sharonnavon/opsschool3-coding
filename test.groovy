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
            sh "mvn package"
           }
        }
    }
}
