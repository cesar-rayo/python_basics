#Jenkins for python 3.X
FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
USER jenkins

#sudo docker image build -t jenkins .
#sudo docker run --name jenkins -p 8080:8080 jenkins
