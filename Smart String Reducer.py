def reduced_string(s:str):
    stack=[]
    for char in s:
        if stack and stack[-1].lower()==char.lower():
            stack.pop()
        else:
            stack.append(char)
    return "" .join(stack)

print("Smart String Reducer")
s=input("ENTER THHE STRING:")
result=reduced_string(s)
print(f"input:{s}and the result:{result}")
