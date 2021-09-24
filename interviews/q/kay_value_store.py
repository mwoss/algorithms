"""
Implement key-value store that has fixed size.
If the store is full remove element that was used the most far in the time. Implement get/put/delete methods.

 * Dict as a key-value store
 * Priority queue (dict with key->pointer, list with elements)
 * The list in priority queue was used to determine priority of the elements
 * Last element in queue has least priority
 * If we use element we repin it to the start of the list
"""