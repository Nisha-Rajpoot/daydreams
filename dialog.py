# interaction with user

print('This is general store where you can buy your food items ')
#card detail
user=''
user=input('Are you new or member:')
import membr_perm as m_p
if user=='new':

#writing application detail
    #import membr_perm as m_p
    m_p.user_detail()

#else:
    #print('please show us the card')




# the buying process begins here
while True:
    try:    
        id=int(input('Enter your member_id please:'))
        #here we ask for if they wish to buy or suggest farmer
        break
        
    except ValueError:
        print('please enter valid id no. ')
#deco to be implemented
bool_val=input('wud you like to provide us some detail of farmers,y or n')
if bool_val=='y':
    m_p.farmer_detail()


    

print('please get your cart for adding items to buy')
print('The list of grocery items available are as follows:')

import groc_item as g
def Show_Item():
    for category in g.grocery_item:
        print(category)
        print('\n')
        
    print('Please pick ur item and add to cart:')
    item=''
    cart_item=list()
    while item!='done':
        item=input('The item u add:')
        cart_item.append(item)
    cart_item.remove('done')    
    print('The food items are:',cart_item)
    #use grep for spelling check snd suggesting items that match nearby
    print('The bill is being calculated,Please wait for a while!')
        
Show_Item()
# here we calculate billncheck if its membr or randm buyer to give special discounts
# we define decorator func call here and decorator wrap func in membr_perm page

