
def class_tree(cls,indent):
    print(indent*'.',cls.__name__)
    for sup_cls in cls.__bases__:
        class_tree(sup_cls,indent+3)

def instance_tree(inst):
    print('Tree of',inst)
    class_tree(inst.__class__,3)


def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E: pass
    class F(D,E): pass

    instance_tree(B())
    instance_tree(F())


selftest()