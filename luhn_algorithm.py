def verify_card_number(card_number):
    card_number = card_number.replace(' ', '').replace('-', '')
    
    digits = [int(d) for d in card_number]

    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        # If the result is greater than 9, subtract 9 (equivalent to summing the digits)
        if digits[i] > 9:
            digits[i] -= 9
    
    total = sum(digits)
    
    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'
