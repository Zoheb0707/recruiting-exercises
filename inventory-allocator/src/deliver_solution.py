'''
    This is the inventory allocator class.
    It attempts to create a minimum cost shipment for the order based on the inventory.
    If successful then a shipment list is returned.
    If it fails then either an exception is thrown or an empty list is returned with
    a helpful message.
'''
class InventoryAllocator :
    
    '''
        This is the Constructor for the InventoryAllocator class.
        It takes a dictionary with an inventory item as key and the number of units as value, 
        and a list of dictionaries as parameters. It then stores them as instance variables.
    '''
    def __init__(self, orders, warehouses):
        
        self.orders = orders
        self.warehouses = warehouses

    '''
        This is a public method of the class.
        It validates the input parameters passed to the constructor.
        Then it extracts information from them.
        Finally it returns a list containing the shipment.
        If the shipment cannot be created then an empty list is returned.
    '''
    def getInventory(self):
        
        orders = self.orders
        warehouses = self.warehouses
        
        if self.__validUserParams():
            warehouse_names, warehouse_inventories, inventory_contents_and_quantity =\
                             self.__extractInfo()
            return self.__generateShipment(warehouse_names, warehouse_inventories,\
                                           inventory_contents_and_quantity)
        else:
            return []
          

    '''
        This is a private method of the class.
        It validates the input parameters passed to the constructor.
        If a parameter is invalid then an error is thrown.
        If a parameter is empty it returns False.
        Else returns True.
    '''
    def __validUserParams(self):
        
        orders = self.orders
        warehouses = self.warehouses
        
        if type(orders) != dict:
            raise Exception('The first parameter should be a dictionary.')
        if type(warehouses) != list:
            raise Exception('The second parameter should be a list.')
        
        if len(warehouses) == 0 and len(orders.keys()) == 0:
            print('Both warehouses and order are empty thus no shipment required.')
            return False
        if len(warehouses) == 0:
            print('Warehouses list is empty thus order cannot be met.')
            return False
        if len(orders.keys()) == 0:
            print('Order is empty thus there is nothing to ship.')
            return False

        return True

    '''
        This is a private method of the class.
        It extracts info from the warehouses list and returns a touple of 3 things.
        It returns a list of warehouse names, a dictionary where the key is the warehouse name
        and the value is the inventory, and a dictionary where the key is an inventory item
        and the value is the total count of that item across all warehouses.
        If an inventory value is not an integer then an error is thrown.
    '''
    def __extractInfo(self):

        orders = self.orders
        warehouses = self.warehouses
        
        warehouse_names = []
        warehouse_inventories = {}
        inventory_contents_and_quantity = {}
        
        for warehouse in warehouses:
            
            warehouse_names.append(warehouse['name'])
            warehouse_inventories[warehouse['name']] = warehouse['inventory']
            
            for element in warehouse['inventory'].keys():
                
                if type(warehouse['inventory'][element]) != int:
                    raise Exception('All item quantities in warehouses list must be integers.')
                if element not in inventory_contents_and_quantity:
                    inventory_contents_and_quantity[element] = warehouse['inventory'][element]
                else:
                    inventory_contents_and_quantity[element] += warehouse['inventory'][element]

        return (warehouse_names, warehouse_inventories, inventory_contents_and_quantity)
    
    '''
        This is a private method of the class.
        It takes a list of warehouse names, a dictionary with keys as warehouse names and
        value as inventory, and a dictionary with keys as inventory items and value as count of item
        across all warehouses.
        It goes through each item in the list of orders and tries to create a minimum cost
        shipment for that item.
        It returns a list of dictionaries where the key is the warehouse name and the value
        is the subset of inventory that should be shipped from that warehouse.
        If the order is not in the keys of the dictionary that stores all inventory then
        an empty list is returned.
        If the order quantity is greater than the quantity present across all warehouses then
        an empty list is removed.
        If the order quantity is not an integer then an exception is thrown.
    '''
    def __generateShipment(self, warehouse_names, warehouse_inventories,\
                           inventory_contents_and_quantity):

        orders = self.orders

        shipment = {}
        deleted_items = []
        
        for order in orders.keys():
            order_value = orders[order]

            if type(order_value) != int:
                raise Exception('All item quantities in orders must be integers.')

            if order not in inventory_contents_and_quantity.keys() and order_value > 0:
                print(str(order) + ' is not available')
                print('No shipment can be created')
                return []
            if order_value <= 0:
                deleted_items.append(order)
                continue
            if order_value > inventory_contents_and_quantity[order]:
                print(str(order_value) + ' ' + str(order) + 's not in inventory')
                print('No shipment can be created')
                return []

            warehouse_index = 0
            while order_value > 0:
                warehouse = warehouse_names[warehouse_index]
                warehouse_index += 1

                if order in warehouse_inventories[warehouse].keys():
                    quantity_contained = warehouse_inventories[warehouse][order]
                    to_add = 0
                    if quantity_contained >= order_value:
                        warehouse_inventories[warehouse][order] -= order_value
                        to_add = order_value
                        order_value = 0
                    else:
                        warehouse_inventories[warehouse][order] = 0
                        to_add = quantity_contained
                        order_value -= quantity_contained
                    if warehouse in shipment.keys():
                        shipment[warehouse][order] = to_add
                    else:
                        shipment[warehouse] = {order:to_add}

        if len(deleted_items) > 0:
            print('The following items were removed as their quantities were invalid')
            print(deleted_items)
        return self.__convert(shipment)

    '''
        This is a private method of the class.
        It takes in a dictionary which represents a shipment.
        It then converts this dictionary to a list of dictionaries and returns it.
    '''
    def __convert(self, shipment):
        converted_shipment = []
        for key in shipment.keys():
            converted_shipment.append({key:shipment[key]})
        return converted_shipment
        
