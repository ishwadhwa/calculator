print("Pls select opreation-\n"\
"1.Add\n"\
"2.subtract\n"\
"3.multiply\n"\
"4.divide\n");
select=int(input("select opreation from 1,2,3,4:"))
number_1=int(input("enter first number:"));
number_2=int(input("enter second number:"));
if select == 1:
    print(number_1, "+", number_2, "=",
                    number_1+number_2)
elif select==3:
    print(number_1,"*",number_2,"=",
                      number_1*number_2)
elif select==4:
    print(number_1,"/",number_2,"=",
          number_1/number_2)
elif select==2:
    print(number_1,"-",number_2,"=",
                number_1-number_2)
else:
    print("invalid input")
                