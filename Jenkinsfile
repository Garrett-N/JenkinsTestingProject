#!/usr/bin/env groovy
pipeline {
    agent {
        node {
            label 'main'
        }
    }
    stages {
        stage('Initialize') {
            steps {
                script {
                    def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }
        stage('build') {
            agent { docker { image 'python:3.9.2-alpine3.13'}}
            steps {
                sh 'pip install -r requirements.txt && python ${WORKSPACE}/src/test.py'
            }
        }
        stage('Docker Image') {
            steps {
                sh 'docker build -t personal-python-test . '
            }
        }
        stage('Run Image / Container Creation') {
            steps {
                sh 'docker run -p 5000:5000 -d --name myfirstcontainer person-python-test'
            }
        }
    }
}