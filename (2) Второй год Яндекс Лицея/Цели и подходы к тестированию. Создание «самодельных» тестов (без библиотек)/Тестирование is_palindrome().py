from yandex_testing_lesson import is_palindrome

print('YES' if [True, True, True, False, False, True, True, False, False, False] ==
               [
                   is_palindrome(i)
                   for i in ['', 'e', 'gwEG', 'EWG', 'gg', 'ds', 'a c b b c a', 'цкпцы', 'пыв', 'тататвы']
               ] 
      else 'NO')