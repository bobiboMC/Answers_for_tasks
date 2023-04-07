
def priceCheck(products, productPrices, productSold, soldPrice):
    #check if input size of products and productSold is correct
    if not (1 <= len(products) <= 99 and 1 <= len(productSold) <= 99):
        return "Error: Invalid input size"
    
    #check if all prices are valid
    for price in productPrices + soldPrice:
        if not (1.00 <= price <= 100000.00):
            return "Error: Invalid price value"
    
    #check if a sold product is a product we have in our products list
    for sold in productSold:
        if sold not in products:
            return "Error: Invalid product name"
    
    #count errors of sale prices that were entered incorrectly
    count_errors = 0
    for i in range(len(productSold)):
        idx = products.index(productSold[i])
        if soldPrice[i] != productPrices[idx]:
            count_errors += 1
    return count_errors


if __name__ == "__main__":
    #Test 1 for function priceCheck(products, productPrices, productSold, soldPrice)
    products=['rice', 'sugar', 'wheat', 'cheese']
    productPrices=[16.89, 56.92, 20.89, 345.99]
    productSold=['rice', 'cheese']
    soldPrice=[18.99, 400.89]
    num_of_errors=priceCheck(products, productPrices, productSold, soldPrice)
    print("Test1:",num_of_errors)
    #Test 2 for function priceCheck(products, productPrices, productSold, soldPrice)
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    num_of_errors=priceCheck(products, productPrices, productSold, soldPrice)
    print("Test2:",num_of_errors)