# -*- coding:utf-8 -*-

import json

class ObjEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, obj):
            return o.__dict__
        try:
            return json.JSONEncoder.default(self, o)
        except Exception as e:
            return o.__str__()
    
class obj():
    def __str__(self):
        return json.dumps(self, sort_keys=True, indent=2, cls=ObjEncoder)
    pass

def func():
    print 'func'

def test():
    a = obj()
    a.name = 'james'
    a.code = '007'
    a.func = func
    a.num = 10
    b = obj()
    b.x = 'x'
    b.func = func
    a.list = [1,2,4]
    a.dic = {'b':b}
    a.float = float(1.2)
    a.long = long(200)
    a.b = b
    print a

if __name__ == '__main__':
    test()

'''
{
  "b": {
    "func": "<function func at 0x102e35320>", 
    "time": "2018-02-23 19:27:14.669398", 
    "x": "x"
  }, 
  "code": "007", 
  "float": 1.2, 
  "func": "<function func at 0x102e35320>", 
  "list": [
    1, 
    2, 
    4
  ], 
  "long": 200, 
  "name": "james", 
  "num": 10
}
[Finished in 0.1s]
'''
