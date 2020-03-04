# we define here the function that takes detail of user

def user_detail():
    print('''we provide local products with purity and preservation based on ancient ways 
    We allow our buyers to  enjoy the discounts as wel as suggest local farmers from nearby''')
    print('please provide few details for membership')
    name=str(input('Name:'))
    address=str(input('address:'))
    phone_nu=input('phone no. ')
    email_id=input('email id:')
    user_detail=(name,address,phone_nu,email_id,)
    print(user_detail)

#we try creating user id from name and address
    user_id_nu=0    
    user_id=name[0:2]+'_'+address[0:2]
    user_id_nu+=1
    print('Thank you for letting us serve you \n your user id :',user_id_nu)
    
#we need a function that gets farmers for produce from nearby
def func_deco(func_fdetail):
    def wrap_func():
        print('We let our members to bring local farmer produce too\
                    supporting the philosophy of ''food from farm on table')
    
        func_fdetail()
        print('please proceed with buyings,happy shopping :)')
    return wrap_func

# detail and farmer detail
@func_deco
def farmer_detail():
    name=input('The farmer name is:')
    address=input('The address:')
    contact_nu=input('The contact number is:')
    print('The farmer detail you provided are:',name,address,contact_nu)
