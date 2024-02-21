def top_n(items, n):
    """Return the top n items in an array, in desc order.

    Args:
        items (array): list or array-like object
        n (int): num of items to return

    Return:
        arrary: top n items, in desc order

    Egs:
        >>> top_n([8,3,4,7,2], 3)
        [8,7,4]
    """
for i in range(n): #keep sorting until we have top n items
    for j in range(len(items)-1-i):
      
        if items[j] > items[j+1]: # if this item is bigger that next item...
            items[j], items[j+1] = items[j+1], items[j] # swap the tw0!

        # get last two items
        top_n =items[-n:]
        
        #return in descending order
        return top_n[::-1]