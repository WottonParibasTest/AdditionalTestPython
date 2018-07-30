from Product import *
from functools import reduce
from math import floor

def main():
    apple = Product("Apple", 0.20)
    orange = Product("Orange", 0.50)
    watermelon = Product("Watermelon", 0.80)

    basket = [ProductInstance(apple, 4), ProductInstance(orange, 3), ProductInstance(watermelon, 5)]
    three_for_two = list(filter(lambda p: p.product.name == "Watermelon", basket))
    bog_of = list(filter(lambda p: p.product.name == "Apple", basket))

    format_decimal = lambda x : format(x, '.2f')

    for p in basket:
        for count in range(0, p.count):
            print("{0: <40} £{1}".format(p.product.name, format_decimal(p.product.price)))

    print()

    discount_total = 0.0
    total_before_discount = reduce(lambda a, b: a + b, map(lambda x: x.count * x.product.price, basket))
    if three_for_two or bog_of:

        print("Total before discount is: £{}".format(format_decimal(total_before_discount)))

        if three_for_two:
            for p in three_for_two:
                free_count = floor(p.count / 3)
                if free_count > 0:
                    discount = free_count * p.product.price
                    discount_total += discount;
                    print("3 for 2 on {}, {} free, save £{}".format(p.product.name, free_count, format_decimal(discount)))

        if bog_of:
            for p in bog_of:
                free_count = floor(p.count / 2)
                if free_count > 0:
                    discount = free_count * p.product.price
                    discount_total += discount;
                    print("BOGOF on {}, {} free, save £{}".format(p.product.name, free_count, format_decimal(discount)))

        print("Total discount £{}".format(format_decimal(discount_total)))

    print("Balance to pay £{}".format(format_decimal(total_before_discount - discount_total)))

if __name__=="__main__":
    main()