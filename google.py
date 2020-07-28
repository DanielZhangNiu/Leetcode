
Q: Given a product name and an offer title, write a function that finds and returns an alias (a permutation of the consecutive product name tokens) from the offer title.


Example 1)
product name: lg g4 smartphone
offer title: lg smartphone g4 64gb white

the function takes the product name and the offer title and then returns "lg smartphone g4"

Example 2)
product name: lg g4 smartphone
offer title: google apple lg g4 smartphone g4 64gb

the function does not return an alias because there is no alias.

def find_alias(p_name, title):
    p_table = collections.defaultdict(int)
    t_table = collections.defaultdict(int)
    length = len(p_name)
    for ele in p_name:
     p_table[ele]+= 1
       #{l:1, g:1, sma:1}
    
    for i in range(length):
       t_table[title[i]]+= 1
       #{go:1, a:1, l:1}

    if t_table == p_table:
       return “”.join(title[:length])

    #{g:1, sma:1, l:1}
    for i in range(1, len(title)-length):
        t_table[title[i+length]] += 1
      t_table[title[i-1]] -= 1
        if t_table[title[i-1]] == 0:
           del t_table[title[i-1]]

        if t_table == p_table:
            return “”.join(title[i : i + length - 1])

    return “”
    
    
    l ,r, cnt = 0, 0 , len(p_table)
    idx = 0
    minlen = sys.maxsize
    while r < len(title):
        if p_table[title[r]] > 0:
            cnt -= 1
            p_table[title[r]] -=1
        while cnt == 0:
            if r - l < minlen:
                minlen = r - l
                idx = l

          if p_table[title[l]] == 0:
            cnt += 1

        p_table[title[l]] += 1
         l += 1

      else:
        p_table[title[l]] -= 1
      r + 1

    return title[idx:idx + length] if minlen != sys.maxsize else “”
        

    
    #return None if len(t_table)!= len(p_table)
    

    #return p_name if t_table == p_table


