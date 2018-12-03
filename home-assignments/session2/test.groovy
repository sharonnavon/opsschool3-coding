node ('aws_dyn_slave'){
  echo 'Strating weather script:'

  stage('Checkout'){
       dir('dir3') {
           git url: 'https://github.com/sharonnavon/opsschool3-coding.git'
       }
  }

  sh '''
        #!/bin/bash
        cd /home/ubuntu/workspace/weather_cli_pipeline_direct/dir3/home-assignments/session2
        ls -l
        pwd
     '''
}