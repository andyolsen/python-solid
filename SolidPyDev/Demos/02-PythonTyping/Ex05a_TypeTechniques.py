from typing import Optional, Any


def f1(a: str | int | float) -> str :
    if type(a) is str:
        return "str received, with value " + a
    elif type(a) is int:
        return "int received, with value " + str(a)
    else:
        return "float received, with value " + str(a)


def f2(fav_football_team: Optional[str] = None) -> None :
    if fav_football_team is None:
        print("No favourite football team specified, assuming it's Swansea")
    elif fav_football_team == "Swansea":
        print(f"Good choice")
    else:
        print(f"Are you nuts?")


def f3(arg: Any) -> None :
    print(f"f3() received object {arg} of type {type(arg)}")


print(f1("hello"))
print(f1(42))
print(f1(3.14))

f2()
f2("Swansea")
f2("Cardiff")

f3(42)
f3(3.14)
f3("wibble")
f3([10, 20, 30])