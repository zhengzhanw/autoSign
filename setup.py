from distutils.core import setup
import py2exe
import sys


sys.argv.append('py2exe')

packages=[]
py2exe_options = {                                  #py2exe中的options字典
	"includes": ['sip'],
	"dll_excludes": ["MSVCP90.dll",],
	"compressed": 2,
	"optimize": 2,
	"ascii": 0,
	"bundle_files": 3
	}

setup(          #py2exe拓展的distutils setup参数：
	name = '签到',
	windows = ["MyWindow.py",],                                    #列表，包含需要被转换为GUI exe的脚本
	version = '1.0',
	zipfile = None,                      #产生共享压缩文件的名字；可以指定一个子目录：默认是'library,zip'；如果值为none,文件将会被打包进可执行文件而不是library.zip
	options = {'py2exe': py2exe_options}  #字典，
)