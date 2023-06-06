# This program is a letter counter for the number of lowercase and uppercase vowels within a string
# For this task, an extract of the poem 'Jabberwocky' by L. Carroll (1871) has been used as the string

# Step 1: Assigning Txt variable to the poem as a string
Txt = """Twas brillig, and the slithy toves 
      Did gyre and gimble in the wabe: 
All mimsy were the borogoves, 
      And the mome raths outgrabe. 

“Beware the Jabberwock, my son! 
      The jaws that bite, the claws that catch! 
Beware the Jubjub bird, and shun 
      The frumious Bandersnatch!” 

He took his vorpal sword in hand; 
      Long time the manxome foe he sought— 
So rested he by the Tumtum tree 
      And stood awhile in thought. 

And, as in uffish thought he stood, 
      The Jabberwock, with eyes of flame, 
Came whiffling through the tulgey wood, 
      And burbled as it came! 

One, two! One, two! And through and through 
      The vorpal blade went snicker-snack! 
He left it dead, and with its head 
      He went galumphing back. 

“And hast thou slain the Jabberwock? 
      Come to my arms, my beamish boy! 
O frabjous day! Callooh! Callay!” 
      He chortled in his joy. 

’Twas brillig, and the slithy toves 
      Did gyre and gimble in the wabe: 
All mimsy were the borogoves, 
      And the mome raths outgrabe."""

# Step 2: Assigning variables as containers starting at 0 to use in the for loop
lower_vowel = 0
upper_vowel = 0

# Step 3: Start of the for loop which will work through the Txt variable
for i in Txt:
# if-or statement to check the uppercase vowel letters in Txt variable;
# increment by +1 for the upper_vowel container
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        upper_vowel = upper_vowel + 1
# elif statement to check the lowercase vowel letters in Txt variable;
# increment by +1 for the lower_vowel container
    elif i in 'aeiou':
        lower_vowel = lower_vowel + 1
        
# Step 4: Displays the total lower and uppercase vowel letters counted each
print("The number of letters of lowercase vowels is:",lower_vowel)
print("The number of letters of uppercase vowels is:",upper_vowel)

