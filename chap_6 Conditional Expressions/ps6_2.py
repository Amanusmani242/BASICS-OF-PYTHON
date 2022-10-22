#program to find out wether a student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass. assume 3 subjects and take marks as input from the user.
sub1 = float(input("Enter the marks:"))
sub2 = float(input("Enter the marks:"))
sub3 = float(input("Enter the marks:"))

persub1 = (sub1/100)*100
persub2 = (sub2/100)*100
persub3 = (sub3/100)*100
percentage = (sub1+sub2+sub3/300)*100


if(percentage >= 40):
    if(sub1>=33 and sub2>= 33 and sub3>=33):
      print("your pass")
    else:
        print("your failed due to one sub")
else:
    print("your failed due to overall")

