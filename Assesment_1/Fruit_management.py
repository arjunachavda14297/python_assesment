def project():
    print('WELCOME TO FRUIT MARKET')
    print()
    print('''1) Manager
2) Customer
''')
    choice_user=int(input('select your role :'))
    
    if choice_user==1:
        def fruit_market_manager():
            print('Fruit Market Manager')
            print('''
1) Add Fruit Stock
2) View Fruit Stock
''')
            choice_command=int(input('Enter Your Choice :'))
            print()
            if choice_command==1:
                print(f'Add Fruit Stock'.upper())
                fruit_name=input('enter fruit name :')
                fruit_qty=float(input('Enter qty (in Kg) :'))
                fruit_price=float(input('Enter price :'))
                add_fruit=open('add_fruit.txt','a')
                add_fruit.write(f'fruit name :{fruit_name}\nfruit qty (in Kg):{fruit_qty}\nfruit price :{fruit_price}\n\n')
                add_fruit.close()
                print()
                
                yes_no=input('Do you want to perform more operations : press y for yes and n for no :')
                if yes_no=='y':
                    fruit_market_manager()
                else:
                    print('Thank You')
                    pass

            elif choice_command==2:
                print(f'view fruit stock'.upper())
                print()
                view_fruit_stock=open('add_fruit.txt','r')
                all_fruits=view_fruit_stock.read()
                print(all_fruits)
                
                yes_no=input('Do you want to perform more operations : press y for yes and n for no :')
                if yes_no=='y':
                    fruit_market_manager()
                else:
                    print('Thank You')
                    pass

            else:
                print('enter valid input')
                print()
                fruit_market_manager()

        fruit_market_manager()

    elif choice_user==2:
        name=input('Enter your Name :')
        def fruit_market_customer():
            print(f'Welcome {name.upper()} in Fruit market')
            print('''
1)Buy Fruits
2)View Fruits Detail
''')
            choice_command=int(input('Enter Your Choice :'))
            print()
            if choice_command==1:
                def customer_buy_fruit():
                
                    print('Please Select fruit which you want to Buy :')
                    print('''
    1)Apple
    2)Banana
    3)Guava
    ''')
                    choice_command=int(input('Enter Your Choice :'))
                    print()

                    if choice_command==1:
                        qty=float(input('enter qty :'))
                        total_price=float(qty*100)
                        files=open('customer_data.txt','a')
                        files.write(f"customer name : {name}\nfruit name : Apple \nfruit qty : {qty}\n\n")
                        files.close()
                        print('Your Bill')
                        print('--------------------------------')
                        print(f"Fruit Name : Apple\nQuantity : {qty}\nprice :{100}\nTotal price : {total_price}")
                        print('--------------------------------')
                        yes_no=input('Do you want to perform more operations : press y for yes and n for no :')
                        if yes_no=='y':
                            fruit_market_customer()
                        else:
                            print('Thank You')
                            pass
                    elif choice_command==2:
                        qty=float(input('enter qty :'))
                        total_price=float(qty*30)
                        files=open('customer_data.txt','a')
                        files.write(f"customer name : {name}\nfruit name : Banana \nfruit qty : {qty}\n\n")
                        files.close()
                        print('Your Bill')
                        print('--------------------------------')
                        print(f"Fruit Name : Banana\nQuantity : {qty}\nprice :{30}\nTotal price : {total_price}")
                        print('--------------------------------')
                        
                        yes_no=input('Do you want to perform more operations : press y for yes and n for no :')
                        if yes_no=='y':
                            fruit_market_customer()
                        else:
                            print('Thank You')
                            pass
                    elif choice_command==3:
                        qty=float(input('enter qty :'))
                        total_price=float(qty*40)
                        files=open('customer_data.txt','a')
                        files.write(f"customer name : {name}\nfruit name : Guava \nfruit qty : {qty}\n\n")
                        files.close()
                        print('Your Bill')
                        print('--------------------------------')
                        print(f"Fruit Name : Guava\nQuantity : {qty}\nprice :{40}\nTotal price : {total_price}")
                        print('--------------------------------')
                    
                        yes_no=input('Do you want to perform more operations : press y for yes and n for no :')
                        if yes_no=='y':
                            fruit_market_customer()
                        else:
                            print('Thank You')
                            pass
                    else:
                        print('Enter valid Input')
                        customer_buy_fruit()
                customer_buy_fruit()

                        
            elif choice_command==2:
                print(f'view fruits detail'.upper())
                print()
                view_fruit_stock=open('add_fruit.txt','r')
                all_fruits=view_fruit_stock.read()
                print(all_fruits)
                
                yes_no=input('Do you want to perform more operations : press y for yes and n for no :')
                if yes_no=='y':
                    fruit_market_customer()
                else:
                    print('Thank You')
                    pass
            else:
                print('enter valid input')
                print()
                fruit_market_customer()

        fruit_market_customer()

    else:
        print(f'enter valid input'.title())
        print()
        project()


project()
