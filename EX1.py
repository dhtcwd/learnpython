# -*- coding: utf-8 -*- 
import sys
type = sys.getfilesystemencoding()
X = '你好，大蟒蛇'
print X.decode('UTF-8').encode(type)