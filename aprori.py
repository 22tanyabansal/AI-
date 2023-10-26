from itertools import combinations
# Function to generate candidate itemsets of a given size (k)
def generate_candidates(itemset, k):
    candidates = []
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            candidate = list(set(itemset[i]) | set(itemset[j]))
            if len(candidate) == k:
                candidates.append(candidate)
    return candidates

# Function to prune infrequent itemsets
def prune_candidates(candidates, prev_frequent, k):
    pruned_candidates = []
    for candidate in candidates:
        subsets = list(combinations(candidate, k - 1))
        if all(tuple(subset) in prev_frequent for subset in subsets):
            pruned_candidates.append(candidate)
    return pruned_candidates

# Function to find frequent itemsets
def apriori(transactions, min_support):
    itemsets = [[item] for item in set(item for transaction in transactions for item in transaction)]
    frequent_itemsets = []

    k = 1
    while itemsets:
        candidates = generate_candidates(itemsets, k + 1)
        item_counts = {tuple(itemset): 0 for itemset in candidates}
        for transaction in transactions:
            for candidate in candidates:
                if set(candidate).issubset(set(transaction)):
                    item_counts[tuple(candidate)] += 1

        frequent_itemsets.extend([itemset for itemset, count in item_counts.items() if count >= min_support])
        itemsets = prune_candidates(candidates, frequent_itemsets, k + 1)
        k += 1

    return frequent_itemsets

# Sample transactions
transactions = [
    ["apple", "banana", "cherry"],
    ["apple", "banana"],
    ["banana", "cherry"],
    ["apple", "cherry"],
    ["apple", "banana"],
]

# Minimum support threshold (adjust as needed)
min_support = 2

frequent_itemsets = apriori(transactions, min_support)
for itemset in frequent_itemsets:
    # Print the frequent itemset and its support count
    support_count = sum(1 for transaction in transactions if set(itemset).issubset(set(transaction)))
    print(f"{itemset}: {support_count}")




# Apriori algorithm refers to an algorithm that is used in mining frequent products sets 
# and relevant association rules. 
# Generally, the apriori algorithm operates on a database containing a huge number of transactions. 
# For example, the items customers but at a Big Bazar.

# Apriori algorithm helps the customers to buy their products with ease and increases the sales performance of the particular store.

# Components of Apriori algorithm
# The given three components comprise the apriori algorithm.
# Support
# Confidence
# Lift


# Support
# Support refers to the default popularity of any product. 
# You find the support as a quotient of the division of the number of transactions comprising that product by the total number of transactions.
# Support (Biscuits) = (Transactions relating biscuits) / (Total transactions)

# Confidence
# Confidence refers to the possibility that the customers bought both biscuits and chocolates together. 
# Confidence = (Transactions relating both biscuits and Chocolate) / (Total transactions involving Biscuits)

# Lift
# Consider the above example; lift refers to the increase in the ratio of the sale of chocolates when you sell biscuits. 
# Lift = (Confidence (Biscuits - chocolates)/ (Support (Biscuits)