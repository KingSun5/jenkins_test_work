#!/bin/bash
echo "shell build start !"
cd /home/lighthouse/work/jenkins_test_work
git pull
cd tools
python deal_image.py -d ${WORKSPACE} -n ${build_name}