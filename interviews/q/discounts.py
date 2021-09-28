"""
Count the Discounts

You receive two structures as an input:
- A set of products, e.g. products = ["car", "burger", "phone"]
- A list of transactions, e.g. transactions = ["car", "car", "burger", "phone", "car", "phone"]

Imagine a shop selling products given above. That shop has a rule that products having the lowest number of sold items
at a given point in time are sold with a discount.

Having a full history of sold items in transactions, calculate the total count of discounts that were applied.

Example:
["car"*, "car", "burger"*, "phone"*, "car", "phone"*]
Discounts count = 4 (Items with '*' are discounted).

["car"*, "car", "car", "car", "burger"*, "burger", "burger", "phone"*]
Discounts count = 3 (Items with '*' are discounted).
"""

from typing import List


def count_discount(products: List[str], transactions: List[str]) -> int:
    sold_qts = {product: 0 for product in products}
    least_sold_qty = 0
    count = 0
    for transaction in transactions:
        if sold_qts[transaction] == least_sold_qty:
            count += 1

        sold_qts[transaction] += 1

        least_sold_qty = sold_qts[min(sold_qts, key=lambda e: sold_qts[e])]

    return count


def count_discount_optimized(products: List[str], transactions: List[str]) -> int:
    qty_to_products = {0: set(products)}
    product_to_qty = {product: 0 for product in products}
    least_sold_qty = 0
    count = 0
    for transaction in transactions:
        if transaction in qty_to_products[least_sold_qty]:
            count += 1

        curr_qty = product_to_qty[transaction]

        qty_to_products[curr_qty].remove(transaction)
        product_to_qty[transaction] += 1

        if not qty_to_products[least_sold_qty]:
            least_sold_qty += 1

        if curr_qty + 1 not in qty_to_products:
            qty_to_products[curr_qty + 1] = {transaction}
        else:
            qty_to_products[curr_qty + 1].add(transaction)

    return count


if __name__ == '__main__':
    print(count_discount_optimized(["car", "burger", "phone"],
                                   ["car", "car", "burger", "phone", "car", "burger", "phone"]))
    print(count_discount_optimized(["car", "burger", "phone"], ["car", "car", "burger", "phone", "car", "phone"]))
