'''
===================================================================
Project Name    : PlatEMO
File Name       : define_method_name.py
Encoding        : UTF-8
Creation Date   : 2021/11/29
===================================================================
'''

import os
import sys
from collections.abc import Sequence

class FileList(Sequence):
	def __init__(self, target : str) -> None:
		self.target      = target
		self.files     = list()
		self.new_files = list()

	def __getitem__(self, index : int) -> str:
		return self.files[index]

	def __len__(self) -> int:
		return len(self.files)

	# 手法名の置換
	def Replace(self, tentative_name : str, official_name, target : str) -> None:
		for content in os.listdir(target):
			path = os.path.join(target, content)
			if os.path.isdir(path):
				self.Replace(tentative_name, official_name, path)

			if tentative_name in content:
				old_path = os.path.abspath(path)
				new_path = os.path.abspath(os.path.join (os.path.dirname(path), content.replace(tentative_name, official_name)))
				os.rename(old_path, new_path)

def main():
	target = './Data'
	print('変更したい手法の名称を入力してください：', end = '')
	tentative_name = input()
	print('変更後の手法の名称を入力してください　：', end = '')
	official_name  = input()

	fl = FileList(target)
	fl.Replace(tentative_name, official_name, target)

if __name__ == '__main__':
	main()
