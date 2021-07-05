#!/bin/bash
echo "shell build start !"
cd /home/admin/work/jenkins_test_work
git pull
cd tools
python deal_image.py