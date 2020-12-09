import sys
import os
"""
<<global vs nonlocal>>
Ref: https://blog.csdn.net/HappyRocking/article/details/80115241

<<yeild>>
Ref: https://blog.csdn.net/mieleizhi0522/article/details/82142856
為什麼要用生成器？生成器相比一次列出所有的內容的有優勢：   
1.更節省存儲空間  
2.回應更迅速   
3.使用更靈活   

"""
def outer():
    x = 'old'
    def changer():
#        nonlocal x
        x = 'new'
        print("changer():" + x)
    changer()
    print("outer():" + x)


outer()
#print(x)