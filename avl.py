class Node():
    def __init__(self,elt):
        self.elt=elt
        self.n=(None,None)
        self.h=(0,0)
        self.s=(0,0)
    
    def __rep__(self,t,v,b):
        return(t[0],v)if b else(v,t[1])
    
    def __set__(self,node,b):
        self.n=self.rep(self.n,node,b)
        if node:
            self.h=self.rep(self.h,max(node.h)+1,b)
            self.s=self.rep(self.s,sum(node.s)+1,b)
        else:
            self.h=self.rep(self.h,0,b)
            self.s=self.rep(self.s,0,b)
    
    def fix(self,node,b):
        self.set(node,b)
        if abs(self.h[0]-self.h[1])>1:
            z=(self.h[0]-self.h[1])>1
            c=self.n[1-z]
            if c.h[1-z]>=c.h[z]:
                self.set(c.n[z],1-z)
                c.set(self,z)
                return c
            d=c.n[z]
            c.set(d.n[1-z],z)
            self.set(d.n[z],1-z)
            d.set(c,1-z)
            d.set(self,z)
            return d
        return self

    def traverse(self,check,use,ret,x):
        al,ar=((None,0),)*2
        if self.n[0]:
            al=self.n[0].traverse(check,use,ret,x-self.n[0].s[1]-1)
            if al[1]:return(al[0],1)
        a=ret(self,x)
        if check(self,x):return(a,1)
        if self.n[1]:
            ar=self.n[1].traverse(check,use,ret,x+self.n[1].s[0]+1)
            if ar[1]:return(ar[0],1)
        return(use(al,a,ar),0)

class AVL():
    def __init__(self):
        self.h=None

    def trace(self,p,c):
        while p:
            v=p.pop()
            c=v[0].fix(c,v[1])
        self.h=c
    
    def find(self,elt):
        if not self.h:return None
        p,c,x=[],self.h,self.h.s[0]
        while c:
            if elt==c.elt:break
            b=elt>c.elt
            p.append((c,b))
            c=c.n[b]
            x+=(2*b-1)*(c.s[1-b]+1 if c else 0)
        return(p,c,x)

    def get(self,i):
        if not self.h:return None
        if i<0 or i>sum(self.h.s):return None
        p,c,x=[],self.h,self.h.s[0]
        while x!=i:
            b=i>x
            p.append((c,b))
            c=c.n[b]
            x+=(2*b-1)*(c.s[1-b]+1)
        return(p,c)
    
    def add(self,elt):
        if not self.h:
            self.h=Node(elt)
            return 1
        r=self.find(elt)
        c=r[1]
        if c:return 0
        c=Node(elt)
        self.trace(r[0],c)
        return 1
    
    def __deln__(self,p,d):
        if d.n[0]:
            if d.n[1]:
                p.append((d,1))
                c=d.n[1]
                while c.n[0]:
                    p.append((c,0))
                    c=c.n[0]
                d.elt=c.elt
                c=c.n[1]
            else:c=d.n[0]
        else:
            if d.n[1]:c=d.n[1]
            else:c=None
        self.trace(p,c)
    
    def delt(self,elt):
        if not self.h:return 0
        r=self.find(elt)
        if not r[1]:return 0
        self.__deln__(r[0],r[1])
        return 1
    
    def dpos(self,pos):
        if not self.h:return 0
        r=self.get(pos)
        if not r:return 0
        self.__deln__(r[0],r[1])
        return 1

    def disp(self):
        if not self.h:return'[]'
        check=lambda n,x:0
        ret=lambda n,x:str(n.elt)
        z=lambda a:a if a else''
        use=lambda al,a,ar:'['+z(al[0])+a+z(ar[0])+']'
        return self.h.traverse(check,use,ret,self.h.s[0])[0]

class Ulist(AVL):
    def add(self,elt,i=-1):
        if not self.h:
            self.h=Node(elt)
            return 1
        if i<0:
            r=self.get(sum(self.h.s))
            r[0].append((r[1],1))
        else:
            r=self.get(i)
            if not r:return 0
            r[0].append(r[1],0)
        self.trace(r[0],Node(elt))
        return 1
    
    def find(self,elt):
        check=lambda n,x:n.elt==elt
        ret=lambda n,x:x
        use=lambda al,a,ar:-1
        return self.h.traverse(check,use,ret,self.h.s[0])[0]
    
    def delt(self,elt):
        if not self.h:return 0
        a=self.find(elt)
        if a<0:return 0
        self.dpos(a)
        return 1
