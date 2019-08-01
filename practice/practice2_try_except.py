def temp_convert(var):
    try:
        return int(var)
    except ValueError as Arggg:
        print ("参数没有包含数字\n", Arggg)
        
temp_convert("xyz")
print("正常use 應該長這樣")
print("temp_convert(123)=",temp_convert(123))
