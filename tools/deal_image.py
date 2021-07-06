#!/usr/bin/python
#-- coding:utf8 --
import argparse
import os
import sys
from PIL import Image	

RES = "res"

def os_system(cmd):
    print "cmd", cmd
    os.system(cmd)

def init_option():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dst', dest='dst_path', default=False, help='jenkins workspace')
    parser.add_argument('-n', '--name', dest='build_id', default=False, help='build task name')
    args = parser.parse_args()
    return args


def img_to_webp(res_path):
	for root, _, files in os.walk(res_path):
	    for f in files:
	        if os.path.splitext(f)[1] == '.png' or os.path.splitext(f)[1] == '.jpg':
	            fullpath = os.path.join(root, f)
	            if os.path.isfile(fullpath):
    				out_path = os.path.splitext(fullpath)[0] + '.webp'
    				print out_path
    				im = Image.open(fullpath).convert("RGBA")
    				im.save(out_path,"WEBP",lossless = False, quality = 80)
    				print fullpath, out_path
    				os.remove(fullpath)

def init(args):
	global dst_path
	global build_id
	global temp_project
	global item_project
	global res_project
	global tar_project
	# 参数
	dst_path = args.dst_path
	build_id = args.build_id
	# 临时文件夹
	temp_project = os.path.join(sys.path[0],"temp")
	os_system("rm -rf " + temp_project)
	os_system("mkdir " + temp_project)
	# # 预处理文件夹
	item_project = os.path.join(temp_project,build_id) 
	os_system("rm -rf " + item_project)
	os_system("mkdir " + item_project)
	# 拷贝
	res_project = os.path.join(sys.path[0],"..",RES,build_id) 
	os_system("mkdir " + temp_project)
	os_system("cp %s %s" % (res_project, item_project))
	# 转格式
	img_to_webp(item_project)
	# 清理工作空间目录
	tar_project = os.path.join(dst_path,build_id)
	os_system("rm -rf " + tar_project)
	os_system("mkdir " + tar_project)
	# 拷贝到 workspace 
	os_system("cp -r %s %s" % (item_project, tar_project))
	# 清理目录
	os_system("rm -rf " + temp_project)


def main():
    args = init_option()
    print("System action: build start!!!! ")
    print(args)
    init(args)
if __name__ == "__main__":
    main()
