class A:
    def m(self):
        print("A.m")

class B(A):
    def m(self):
        print("B.m")

class X:
    def m(self):
        print("X.m")

class Y(X):
    def m(self):
        print("Y.m")

class MyClass(B, Y):
    ...

# Client code
print("Method resolution order for MyClass:")
print(MyClass.mro())

obj = MyClass()
print("\nMRO decides which method to call:")
obj.m()
print("\nWe can forcibly specify which method to call:")
X.m(obj)