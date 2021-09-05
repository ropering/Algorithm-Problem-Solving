class Singleton(object):
    """
    하나의 싱글톤 인스턴스를 생성
    이미 생성된 인스턴스가 있다면 재사용
    """
    def __new__(cls, *args, **kwargs):
        """
        *args와 **kwargs는 무슨의미일까?
        여러 가변인자를 받겠다고 명시하는 것이며, *args는 튜플형태로 전달, **kwargs는 키:값 쌍의 사전형으로 전달된다.
        def test(*args, **kwargs):
            print(args)
            print(kwargs)
        
        test(5,10,'hi', k='v')
        결과 : (5, 10, 'hi') {'k': 'v'}
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls, *args, **kwargs).__new__(cls, *args, **kwargs)
        return cls.instance

if __name__ == '__main__':
    s = Singleton()
    print("객체 생성", s)
    s1 = Singleton()
    print("객체 생성", s1)



클래스 인스턴스를 메모리에 할당해 “생성” = Allocator, Instantiator

“생성”된 인스턴스를 “사용 준비 시킴” = Constructor, Initializer

__init__은 Constructor, __new__는 Allocator

__new__는 방어적 프로그래밍에 사용 가능

__init__ 메소드는 클래스 오브젝트에 메모리를 할당하지 않는다라는 것
__init__ 메소드는 클래스 인스터스 형태인 객체(Object)가 생성(Created/Instantiated)되어 초기화(Initialized)되는 즉시 호출(Called)되기는 합니다만, 객체에 메모리를 할당하지 않는특수한 메소드
객체에 메모리를 할당(Allocate)하는 주인공은 누구냐? 바로 __new__ 메소드입니다. 파이썬에서 객체를 생성해보면 __init__이 실행되기 전에 항상 __new__가 먼저 실행되며, 이 때 객체에 메모리가 할당됩니다.
__new__메소드는

__init__보다 먼저 실행되며
클래스 자기 자신(cls)을 숨겨진 파라미터로 받으며
반드시 object를 return함

생성자에서 '생성'은 __new__ 메소드로 만든(Instantiate) 인스턴스를 사용자가 원하는 대로 사용하도록 커스토마이징(Customizing/Initiating)함을 말합니다


def __new__(cls,*args,**kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)
        # create our object and return it
        obj = super().__new__(cls)
        return obj
__init__보다 먼저 실행되며
클래스 자기 자신(cls)을 숨겨진 파라미터로 받으며
반드시 object를 return함



class RectPoint(Point):
Point 클래스를 상속했으므로 RectPoint의 클래스 인스턴스는 Point 클래스의 인스턴스이기도 합니다



https://ibit.ly/NeYS __init__ __new__ 차이



def __new__(cls, *args, **kwargs):
여러 가변인자를 받겠다고 명시하는 것이며, *args는 튜플형태로 전달, **kwargs는 키:값 쌍의 사전형으로 전달된다.
test(5,10,'hi', k='v')
결과 : (5, 10, 'hi') {'k': 'v'}


if not hasattr(cls, 'instance'):
hasattr 함수는 cls객체가 instance 속성을 갖고있는지 확인.


# 직접 싱글톤 구현
class Singleton(object):
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
            return self.instance
        return self.instance

a = Singleton()
b = Singleton()

a == b

'''
what is with statement 
https://ibit.ly/sGMK
The with statement clarifies code that previously would use try...finally blocks to ensure that clean-up code is executed. In this section, I’ll discuss the statement as it will commonly be used. In the next section, I’ll examine the implementation details and show how to write objects for use with this statement.

The with statement is a control-flow structure whose basic structure is:

with expression [as variable]:
    with-block
The expression is evaluated, and it should result in an object that supports the context management protocol (that is, has __enter__() and __exit__() methods).
'''

# 각 함수에서 만든 변수도 global하게 접근 가능한가?
class Singleton(object):
    
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
            return self.instance
        return self.instance
    
    def __init__(self):
        print("init")

    def hi(self):
        self.b = "hi"
    
    def hello(self):
        self.c = "hihi"

test = Singleton()
b = Singleton()
test.hi()
test.hello()
test.b
test.c