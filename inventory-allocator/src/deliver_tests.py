from deliver_solution import InventoryAllocator

#test 1
#This test will return [] as there are more apples in the order than in inventory.
#The number of mangoes in order < 1 so it will be ignored.
print('Test 1')
order = {'apple': 11, 'banana': 7, 'mango':0}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 3, 'banana': 7 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = []
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 1: ' + str(expected_output == out))
print()

#test 2
#This test will return [] as there is nothing to order.
print('Test 2')
order = {}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 3, 'banana': 7 } },
              { 'name': 'dm', 'inventory': { 'apple': 5 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = []
out = obj.getInventory()
print('Expected Output: ' + str(expected_output))
print('Output: ' + str(out))
print('Passed Test 2: ' + str(expected_output == out))
print()

#test 3
#This test will return a list of shipments distributed over 2 warehouses as
#the apples need to be distributed.
print('Test 3')
order = {'apple': 11, 'banana': 7}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 9, 'banana': 7 } },
              { 'name': 'dm', 'inventory': { 'apple': 5 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = [{'owd': {'apple': 9, 'banana': 7}}, {'dm': {'apple': 2}}]
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 3: ' + str(expected_output == out))
print()

#test 4
#This test returns a list of shipments from the first warehouse as
#it is the cheapest and it fulfills the order by itself.
print('Test 4')
order = {'apple': 11, 'banana': 7}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 13, 'banana': 7 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = [{'owd': {'apple': 11, 'banana': 7}}]
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 4: ' + str(expected_output == out))
print()

#test 5
#This test returns [] as mango is not present in any warehouse.
print('Test 5')
order = {'apple': 11, 'banana': 7, 'mango': 5}
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = []
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 5: ' + str(expected_output == out))
print()

#test 6
#expected output: This test returns a list of shipments from the first warehouse.
#Note that mango is not in any warehouse however it's value in order is < 1 so it is ignored.
print('Test 6')
order = {'apple': 11, 'banana': 7, 'mango': 0}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 13, 'banana': 7 } },
              { 'name': 'dm', 'inventory': { 'apple': 5 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = [{'owd': {'apple': 11, 'banana': 7}}]
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 6: ' + str(expected_output == out))
print()

#test 7
#This test will throw an exception as the value for mango is not an int.
print('Test 7')
order = {'apple': 11, 'banana': 7, 'mango': 'str'}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 13, 'banana': 7 } },
              { 'name': 'dm', 'inventory': { 'apple': 5 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
print('Expected Output: error')
try:
    obj = InventoryAllocator(order, warehouses)
    print(obj.getInventory())
except:
    print('Output: error')
    print('Passed test 7: True')
print()

#test 8
#This test will return [] as the warehouse is empty.
print('Test 8')
order = {'apple': 11, 'banana': 7}
warehouses = []
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = []
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 8: ' + str(expected_output == out))
print()

#test 9
#expected output: This test will return a list of shipments.
#The shipments are distributed across both warehouses however the cheaper
#warehouse ships most of the elements.
print('Test 9')
order = {'apple': 11, 'banana': 7, 'mango': 4}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 8, 'banana': 7, 'mango': 3 } },
              { 'name': 'dm', 'inventory': { 'apple': 5, 'mango': 3 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = [{'owd': {'apple': 8, 'banana': 7, 'mango': 3}}, {'dm': {'apple': 3, 'mango': 1}}]
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 9: ' + str(expected_output == out))
print()

#test 10
#This test returns an error as the value for banana in the warehouse inventory is
#not an integer.
print('Test 10')
order = {'apple': 11, 'banana': 7, 'mango': 4}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 13, 'banana': True }},
              { 'name': 'dm', 'inventory': { 'apple': 5 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
print('Expected Output: error')
try:
    obj = InventoryAllocator(order, warehouses)
    print(obj.getInventory())
except:
    print('Output: error')
    print('Passed test 10: True')
print()

#test 11
#This test returns a list of shipments. The shipment is from the first warehouse only.
#This is because there are enough bananas in the first warehouse and apples is deleted
#from the order as its value is less than 1.
print('Test 11')
order = {'apple': -1, 'banana': 7}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 13, 'banana': 7 } },
              { 'name': 'dm', 'inventory': { 'apple': 5 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = [{'owd': {'banana': 7}}]
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 11: ' + str(expected_output == out))
print()

#test 12
#This test returns a list of shipments. The shipment is split over 2 warehouses
#in order of cost.
print('Test 12')
order = {'apple': 10, 'banana': 9}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 13, 'banana': 7 }},
              { 'name': 'dm', 'inventory': { 'apple': 5, 'banana': 4 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = [{'owd': {'apple': 10, 'banana': 7}}, {'dm': {'banana': 2}}]
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 12: ' + str(expected_output == out))
print()

#test 13
#This test returns a list of shipments. THe shipment is split over 3 warehouses
#in order of cost.
print('Test 13')
order = {'apple': 10, 'banana': 6}
warehouses = [{ 'name': 'owd', 'inventory': { 'apple': 13, 'banana': 4 }},
              { 'name': 'dm', 'inventory': { 'apple': 5, 'banana': 1 }},
              {'name': 'dm2', 'inventory':{'banana': 5, 'apple': 4 }}]
print('Inputs: \n' + str(order) + '\n' + str(warehouses))
obj = InventoryAllocator(order, warehouses)
expected_output = [{'owd': {'apple': 10, 'banana': 4}}, {'dm': {'banana': 1}},
                   {'dm2': {'banana': 1}}]
print('Expected Output: ' + str(expected_output))
out = obj.getInventory()
print('Output: ' + str(out))
print('Passed Test 13: ' + str(expected_output == out))
print()
