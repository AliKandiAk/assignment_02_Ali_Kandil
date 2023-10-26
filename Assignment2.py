def CountDigits(n):
  if n<10:
    return 1
  else:
    return 1+CountDigits(n/10)
def FindMax(lis):
    if len(lis)==1:
        return lis[0]
    else:
      max=FindMax(lis[1:])
      if lis[0]>max:
         return lis[0]
      else:
         return max
def Count_Tags(html_code, tag):
    start_tag = f"<{tag}>"
    end_tag =f"</{tag}>"
    
    start_index = html_code.find(start_tag)
    end_index = html_code.find(end_tag)
    
    if start_index == -1 or end_index == -1:
        return 0
    
    return 1 + Count_Tags(html_code[end_index+len(end_tag):], tag)

while True:
    print("1.Count Digits:")
    print("2.Find Max:")
    print("3.Count Tags:")
    print("4.Exit:")  
    x = input('Enter a number: ')
    
    if x == "1":
        a = input("Enter a number to count: ")
        digit_count = CountDigits(eval(a))
        print(f"The number of digits in {a} is: {digit_count}")
    
    elif x == "2":
        my_list = []
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            ele = int(input())
            my_list.append(ele) 
        max_value = max(my_list)
        print(f"The maximum value in the list is: {max_value}")
        
    elif x == "3":
        tag = input("Enter tag: ")
        html_string = input("Enter an HTML string: ")
        tag_count = Count_Tags(html_string, tag)
        print(f"The number of '{tag}' tags in the HTML code is: {tag_count}")
        
    elif x == "4":
        break

    else:
        print("Invalid input. Please enter a valid number.")
