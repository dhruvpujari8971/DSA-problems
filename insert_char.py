# inserting the new character in the string at accurate position

string='hello'
char_to_add='t'
new_char_pos=3


new_string = string[:new_char_pos] + char_to_add + string[new_char_pos:]
print(new_string)

      
    
      
    
   
    