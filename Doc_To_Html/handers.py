#_*_ coding: utf-8 _*_

class Hander:
    '''
    生成HTML的具体处理程序的泛型方法实现.
    '''
    def callback(self,prefix,name,*args):
        method=getattr(self,prefix+name,None)
        if callable(method):
            return method(*args)

    def start(self,name):
        self.callback('start_',name)

    def end(self,name):
        self.callback('end_',name)

    def sub(self,name):
        def substitution(match):
            result=self.callback('sub_',name,match)
            if result is None:
                #如果找不到sub_name方法 走这个分支
                result=match.group(0)
            return result

        return substitution


class HTMLRender(Hander):
    '''
    用于生成HTML的具体处理程序

    HTMLRender内的方法可以通过超类处理程序start(),end(),sub()方法
    来访问，它们实现了用于HTML文档的基本标签.
    '''

    def start_document(self):
        print '<html><head><title>...</title><body>'
    def end_document(self):
        print '</body></html>'
    def start_paragraph(self):
        print '<p>'
    def end_paragraph(self):
        print '</p>'
    def start_heading(self):
        print '<h2>'
    def end_heading(self):
        print '</h2>'
    def start_list(self):
        print '<ul>'
    def end_list(self):
        print '</ul>'
    def start_listitem(self):
        print '<li>'
    def end_listitem(self):
        print '</li>'
    def start_title(self):
        print '<h1>'
    def end_title(self):
        print '</h1>'

    def sub_emphasis(self,match):
        return '<em>%s<em>' % match.group(1)
    def sub_url(self,match):
        pass
    def sub_mail(self,match):
        pass

    def feed(self,data):
        print data





