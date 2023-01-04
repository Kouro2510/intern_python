def toCamelCase(str):  
    #Xóa khoảng cách hoặc dấu ở gần các chữ
   string = str.replace("-", " ").replace("_", " ")  
    #tách chuỗi ký tự
   string = string.split()

   if len(str) == 0:

       return str

   return string[0] + ''.join(i.capitalize() for i in string[1:])

   

print(toCamelCase("the-stealth-warrior"))