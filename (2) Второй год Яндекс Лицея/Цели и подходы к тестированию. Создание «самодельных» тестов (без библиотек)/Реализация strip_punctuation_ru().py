def strip_punctuation_ru(data):
    P = (',',
         '.', 
         ':',
         ';', 
         '!', 
         '?', 
         '...',
         ' - ')
    for m in P:
        data = data.replace(m, " ").strip()
    return data