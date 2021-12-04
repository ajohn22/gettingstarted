def welcome_assignment_answers(question):
     if question == "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
        answer = "mTLS"


     if question == "Are encoding and encryption the same? - Yes/No":
       answer = "No"


     if question == "Is it possible to decrypt a message without a key? - Yes/No":
       answer = "No"


     if question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"


     if question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"


     if question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        answer = "42B76FE51778764973077A5A94056724"
        answer.isalnum()


     if question ==  "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"


     if question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer = int(5)


     if question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = int(4)

     return (answer)