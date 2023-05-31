# GPTProMoat
A privacy focused LLM data obfuscation tool that implements end-to-end encryption and prevents retraining on company data by GPT-4

Step 1: Research Agent
1.1. Research different encryption algorithms and their strengths and weaknesses.
1.2. Evaluate the suitability of each algorithm for the given task.
1.3. Identify potential vulnerabilities in each algorithm.
1.4. Document the research findings and present them to the Manager Agent.

Step 2: Encryption Agent
2.1. Based on the research findings from the Research Agent, select the most suitable encryption algorithm.
2.2. Develop the code for the encryption algorithm.
2.3. Test the encryption algorithm to ensure it is functioning correctly.
2.4. Document the encryption algorithm and present it to the Manager Agent.

Step 3: Decryption Agent
3.1. Develop the code for the decryption algorithm that corresponds to the encryption algorithm selected by the Encryption Agent.
3.2. Test the decryption algorithm to ensure it is functioning correctly.
3.3. Document the decryption algorithm and present it to the Manager Agent.

Step 4: Manager Agent
4.1. Evaluate the encryption and decryption algorithms developed by the Encryption and Decryption Agents.
4.2. Determine if any changes or improvements need to be made to the algorithms.
4.3. Coordinate with the Research Agent to identify any potential vulnerabilities in the algorithms and implement any necessary security measures.
4.4. Document the final encryption and decryption algorithms and present them to the client or stakeholders.

Please note that this is a high-level overview of the steps. The actual implementation will depend on the specific requirements of the task and the findings of the Research Agent.


## Original Data generated with Faker

|    | name             | address                                                | email               | phone_number         | social_security_number   | job                                      | company                       | residence                                            | current_location                                      | website                         | username       |   age | gender   |   Grades | preferred_language   | preferred_currency   | job_title                                |   national_id |   height |   weight |
|---:|:-----------------|:-------------------------------------------------------|:--------------------|:---------------------|:-------------------------|:-----------------------------------------|:------------------------------|:-----------------------------------------------------|:------------------------------------------------------|:--------------------------------|:---------------|------:|:---------|---------:|:---------------------|:---------------------|:-----------------------------------------|--------------:|---------:|---------:|
|  0 | Lindsay Espinoza | 496 Christine Keys Suite 765, Rebeccaborough, NM 21368 | carolyn99@gmail.com | 001-813-618-2068x668 | 462-12-1554              | Librarian, public                        | Myers, Walton and Hamilton    | Unit 9931 Box 7724, DPO AP 19226                     | 0412 Wilson Loop Apt. 941, Jennifertown, MP 63087     | https://smith.com/              | lauriecooper   |    60 | F        |       54 | apn                  | HUF                  | Librarian, public                        |    7715080717 |      151 |      135 |
|  1 | Amanda Sharp     | 80527 Lynn Creek Suite 765, Ericmouth, CT 11608        | kristy26@gmail.com  | 551.323.1535x7432    | 658-88-2634              | Tourism officer                          | Wright Group                  | 185 Robert Heights Apt. 954, Romerostad, FM 02348    | 39064 Brian Forge Apt. 873, Comptonborough, NE 06729  | https://www.roberts.info/       | fernandezkevin |    60 | F        |       88 | nds                  | SGD                  | Tourism officer                          |    8706937496 |      157 |      119 |
|  2 | Daniel Hunt      | 320 Sawyer Forge, Sanchezmouth, PA 09126               | jjohnson@yahoo.com  | 6546061210           | 423-95-5798              | Conservation officer, historic buildings | Davis Inc                     | 2155 Brianna Stravenue, Montgomeryshire, CO 93842    | 1836 Lee Parks Suite 073, South Gregoryview, IA 16966 | https://www.thompson.com/       | juliepatterson |    80 | M        |       90 | ja                   | XCD                  | Conservation officer, historic buildings |    8004325092 |      141 |      181 |
|  3 | Kyle Barrera     | 20210 Smith Corner, East Alexandramouth, MN 47018      | kevin59@gmail.com   | 001-416-361-2263     | 244-08-5241              | Animator                                 | Romero Group                  | 9166 Bartlett Fall Suite 487, Lake Annaton, GU 06226 | 67254 Bowman Ford Suite 889, North Kelly, PR 68231    | http://www.johnson-hoover.info/ | scottscott     |    79 | M        |       90 | nhn                  | VND                  | Animator                                 |    6250358185 |      154 |      193 |
|  4 | Elizabeth Walker | 3014 Janet Prairie, Lake Richardberg, OR 42861         | lisa09@hotmail.com  | 963.312.8349         | 564-90-8666              | Consulting civil engineer                | Hernandez, Dorsey and Skinner | 1897 Weber Isle Suite 454, Brownton, MD 38173        | 121 Flores Street Apt. 968, East Jessica, CT 33159    | https://stewart.com/            | randyjuarez    |    23 | F        |       52 | hi                   | TTD                  | Consulting civil engineer                |    8384461116 |      145 |      191 |

## Encrypted Data

|    | name                     | address                                                                  | email                        | phone_number                 | social_security_number   | job                                                      | company                                  | residence                                                                | current_location                                                         | website                                      | username             | age   | gender   | Grades   | preferred_language   | preferred_currency   | job_title                                                | national_id      | height   | weight   |
|---:|:-------------------------|:-------------------------------------------------------------------------|:-----------------------------|:-----------------------------|:-------------------------|:---------------------------------------------------------|:-----------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|:---------------------------------------------|:---------------------|:------|:---------|:---------|:---------------------|:---------------------|:---------------------------------------------------------|:-----------------|:---------|:---------|
|  0 | JObj0xm0Q2H0iClInf0o4g== | YaH3WFy9ye+mFl8Y/PxFxv2APGYSlWs/seAF6vtsjZc+SlRWlO/JE1cIEHhmsNNjDChj3sOF | xVN16wr8EYUIuXh6qpw7kqHVzg== | ePwo3hG+rf2UfoqEfOKULpAcfTc= | ViDUfZael9tcRDM=         | Qni+V18JkT5TTO6KJPlXn3A=                                 | j6k9CONe/qCsk0+j4nVCdtAxRbwepBcvCPQ=     | ENiq4JY8TFLNXuZjDqBj/eQh6yBs7VvGLSmZFHcvg4w=                             | QxlXOCFfao80vyDC7iLv1pVevmf+1lBy8MkjCP6q5JF326M4C5AldxPpNyfTjAJ5Qg==     | Pw75yMfV5RSJooJrNbhgL/oh                     | 4pcFpij0B59lZtIu     | DbM=  | MA==     | YJk=     | SEce                 | AnAI                 | S63BlSX9OzAmVePA9VUqqSg=                                 | q8FaG55YL5Pv+A== | xrQu     | vm7H     |
|  1 | mkjdIFRD8eVvCZpK         | ggIGLNy7N2xc+w7198xFJdahymKLiz1gt+DjussAxNPUWhdNXsFj3Ji97Lh8Pz8=         | 5kST9fRcf8TqfacXeVXAYDo/     | IURhcTL5pIu1VLqE3z8ypD0=     | PB+qBzfT0ICltI8=         | Ptpgp1icqvl8PwjZLsmh                                     | ofa5iLblzs0l9L2O                         | i2+a/fUYYsxjuqTR6+YDbgmBW+XCm0dGJIquAJ3eTemP7fCoErhICy8Xl39XitXeXQ==     | H4fUOfcOWvXlQ0gyLALeyUQ8f+FaTC7DX6aEwSkGDJtE8XGC5Y5GlJ+Q80spGSOfNF3O+A== | /eWh9VVcHpdYJ7cxdwGq8zFWBhWmcXERzA==         | P88aujfNOVAAeMTGrV0= | REk=  | hw==     | pcA=     | 483k                 | 522L                 | FSdyP2mvHV1MrRrt9AOv                                     | YvyTbNyoXxCRKg== | wvcg     | d0xQ     |
|  2 | 7fL/BXs0kt6njnI=         | 1ANXOmhJEqT+8n6I+bRkx/ufPHHokoT/8gKge0Z3/pLEdckWxEXWMw==                 | a5CJQfLS503w8UsL7avLNNFH     | L+L25LlsxIfdFg==             | 9mJn/eT7qvlUKY0=         | AlMVqmpD6VbT+j1LZ368/Sv8sQFexifCH/qpK7xqqCx1FYK1+v18mw== | sln2Z4fJmz9L                             | coytNHoiadMA7w7MxRLxDwU7lFakyuAov+afV8Xqt4VmyTrAIg6pUblU5AQQ1A3RDQ==     | qRAQugnybOHz6l6UuBXwreenOg2oClQzsVAnlGf9E9TVfBYtIwDXEpfWQEgnCClVD/oFJOk= | vpMRoLo5rBB//xcGJQwf2UyffOqq8BPFnQ==         | 4KT2tAf8dkrVJZQjvtg= | BMQ=  | 7Q==     | Ei4=     | +Uo=                 | sGZY                 | szffA0fM/VikDDqtxN4hug24F2eMouboXlVPcsEyodwF0pHtFNeR2g== | wz2VHlPHme+n4w== | IPVe     | R1/z     |
|  3 | 7Kj382WuCbBvSugH         | de87O3rlp1RtELq3TShqjTWI7xLIccWgHuOkckNE8cmX/Jxk1F+JZWeC1k9ADZNVDQ==     | NdVI6wnVYJLmGs8LQwqToho=     | DqPqUZs69LyS6pNus86ciQ==     | kvW1yUoNC9KqI4Q=         | mNdkASPTG/Q=                                             | bRGHJC+/22n3gDxP                         | Zim9K1uJEZb5XOTF2KljHJ4cAdvAZXcncOeH/qJ9DtM+uRaZ6h14c4lcxWMcThBivXGyIQ== | qV5tVt6ESk8k0Bl1q5ZGXEq9996nTLjAXOoNlPVkJpJjQtB02gcVJx4MvN15oEe1UPM=     | 5XbQQ+gfD4JEsyiqyYIQ/zKtsFDtynxAu/zKYdhPtQ== | 9RLK8qa/kk+27Q==     | ATM=  | Lg==     | nUE=     | qrh3                 | lW30                 | dRA235q+A2s=                                             | xJnRg/nnwdC83A== | JqE5     | D+Kc     |
|  4 | LPLR9t7oa06RxB06bJFgUg== | LEGuf/EuoMkOMUL6M5vs1Ob6DJKNO5oPIyV1JDwXU01Px7rrYMhdND10bEyPog==         | HpMpoZ8/SdT20ttw+6VwZ/Rt     | 2DlyfJkoiCtHYY2j             | whvMENvzh6rlZmU=         | 3+FuM7bK4590KfAIZVDJJKotXVjSfa0qzA==                     | RgYCJyNKkSNgwmHb2Z8TC/Z8XuexzqPi+B7GXU0= | PujmA9gM2/mvRnI1o1LDQMwn80Q4rWMcCVNl9IiQFyg42KE9Aaz4eb7rlWxT             | wgr7KXG3dmliQWHYO8ZhMsDvdrJQ2wNEmfIezyZmGqW/u3T6WrLdLcNzYzIme2RvVEA=     | 5B2qjoAXnpScYchgNfhuDqri9gk=                 | WU7dpv8ptTQaWRs=     | t1U=  | vQ==     | N7o=     | fsA=                 | SUFY                 | GsTiJGGWm/A55rzYWW9PRPSpVvd9c3m3Uw==                     | lYQa8CqXagCU4w== | utYh     | YGGZ     |