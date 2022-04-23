def search(phrase:str='hello world',letters:{}=set('aeiou'))->str:
    return str(sorted(set(phrase).intersection(letters)))


