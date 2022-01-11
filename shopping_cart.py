class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None, total = 0 ,  items = []):
      self.total = total
      self.employee_discount = emp_discount
      self.items = items
      
    def add_item(self, name, price, quantity=1):
       
       self.total += price*quantity
       list_of_items = [name, price, quantity]
       self.items.append(list_of_items)
       return price*quantity
   
       
    def mean_item_price(self):
       number = sum([int(item[2]) for item in self.items])
       return self.total/number


    def median_item_price(self):
        number_list = sorted([int(item[1]) for item in self.items])
        print(number_list)
        if (len(number_list) % 2) != 0:
           return number_list[int(len(number_list)/2) + 1]


    def apply_discount(self):
       if self.employee_discount:
          return self.total * (1-self.employee_discount/100)
       else:
          return "Sorry, no discount"

    def void_last_item(self):
        pass