#_*_ coding: utf-8 _*_

def lines(file):
    for line in file:
        yield line
    yield '\n'

#文本块生成器
#先理解文本块生成的处理方式(包含存在多个空行的情况)
def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block)
            block=[]

if __name__=='__main__':
    f=open(r'D:\03F_DISK\test.log','r')
    for block in blocks(f):
        print block
    print "file over"
