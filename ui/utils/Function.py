def firstDegree(a,b):
    if a==0 and b==0:
        return "Infinity!"
    elif a==0 and b!=0:
        return "No Solution!"
    else:
        x=-b/a
        return f"x={x}"