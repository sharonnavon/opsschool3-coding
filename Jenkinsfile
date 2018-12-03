pipeline{
    agent {label 'aws_dyn_slave'}

    stages{
      stage('---checkout---'){
        steps{
            sh '''
            #!/bin/bash
            cd /home/ubuntu/workspace/weather_cli_pipeline_direct/home-assignments/session2
            ./cli.py --city tel-aviv --forecast TODAY+3 -c
            '''
        }
      }
    }
}
