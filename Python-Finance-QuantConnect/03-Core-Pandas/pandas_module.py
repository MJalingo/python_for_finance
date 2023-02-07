def with_billion(bill):
    '''
    using the float() function
    '''
    cut = str(bill)
    if (bill > 999999999) & (bill < 10000000000):
        '''One billion 1,000,000,000 '''
        bill_cut = float(f"{cut[0]}.{cut[1:]}")
        return(f'{bill_cut:.1f} Billion')
    elif (bill > 9999999999) & (bill < 100000000000):
        '''Two billion 10,000,000,000 '''
        bill_cut = float(f"{cut[:2]}.{cut[2:]}")
        return(f'{bill_cut:.1f} Billion')
    elif( bill > 99999999999) & (bill < 1000000000000):
        '''One billion 100,000,000,000 '''
        bill_cut = float(f"{cut[:3]}.{cut[3:]}")
        return(f'{bill_cut:.1f} Billion')
    
def billion(bill):
    '''
    using the just slicing and indexing
    '''
    cut = str(bill)
    if (bill > 999999999) & (bill < 10000000000):
        '''One billion 1,000,000,000 '''
        bill_cut = (f"{cut[0]}.{cut[1:]}")
        return(f'{bill_cut[:3]} Billion')
    elif (bill > 9999999999) & (bill < 100000000000):
        '''Two billion 10,000,000,000 '''
        bill_cut = (f"{cut[:2]}.{cut[2:]}")
        return(f'{bill_cut[:4]} Billion')
    elif( bill > 99999999999) & (bill < 1000000000000):
        '''One billion 100,000,000,000 '''
        bill_cut = (f"{cut[:3]}.{cut[3:]}")
        return(f'{bill_cut[:5]} Billion')
    
def occurrance(where):
    count = dict()
    for sector in where:
        if sector in count:
            count[sector] += 1
        else:
            count[sector] = 1
            return(count)
def dollar_siqn(*stock_price):
    for price in stock_price:
        if '$' in str(price):
            continue
        else:
            return(f'${price}')