# Project 4
## COP6481 Spring 2024
#### Design a Python function named 'risk_assessment' that
#### takes a string 'transaction_description' as input and returns a risk assessment score



## module : main.py

main() calls the function
+ process_transactions(), passing in a file name and the client
function process_transactions()
+ processes the file that was passed in
+ open the file, and for each line, call assess_transaction_risk()


## module : assess_risk.py

The function assess_transaction_risk()
+ processes each statement and
+ passes it to the openai api with the prompt request
+ to evaluate the risk on scale of 1 – 10
one of the requirements of the exercise was
+ extensive error handling, and
+ assess_transaction_risk() has a try catch, checking for 5 different classes of errors.


## module : config.py
this file contains the function get_openai_client()
which returns the openai client associated with the
private key for the running account. the key is kept in file
.env in the root directory

## Text files
the main file processes three txt files:
+ transactions - random transasction
+ high_assessment – expect to get a high score back
+ low_assement – expect to get a low score score back
High scores indicate high risk.
The high/low files are a test to insure the program is working as expected.

## Program Output

## Random statements
<br>Transaction: Urgent wire transfer needed for overseas client. - Risk Score: 7
<br>Transaction: New regular monthly payment to local supplier detected. - Risk Score: 3
<br>Transaction: Transaction requiring immediate clearance is of high value. - Risk Score: 8
<br>Transaction: Transfering funds between internal accounts. - Risk Score: 2
<br>Transaction: Legal fees are now due and quick payment required. - Risk Score: 7
<br>Transaction: Transaction for consultancy fees needs to be paid in cryptocurrency. - Risk Score: 7
<br>Transaction: New account is attempting money transfer to high-risk country. - Risk Score: 8
<br>Transaction: Cash withdrawal exceeding $10,000 reported. - Risk Score: 7
<br>Transaction: Did you male a charitable donation exceeding $50,000 to an overseas NGO. - Risk Score: 7
<br>Transaction: Your credit card was used to purchase luxury watch from unfamiliar vendor. - Risk Score: 7
<br>Transaction: Repeated multiple transactions totaling $5,000 in the last week. - Risk Score: 8
<br>Transaction: Large payment alert using unverified contractor for unspecified services. - Risk Score: 8
<br>Transaction: Insurance premium payment for new receipient. - Risk Score: 2
<br>Transaction: Refund request from customer claimim=ng double-billed service charge. - Risk Score: 7
<br>Transaction: Monthly rent check has been deposited. - Risk Score: 1
<br>Transaction: Your interest reward has been deposited. - Risk Score: 1
<br>Transaction: Your check printing request has been completed. - Risk Score: 2
<br>Transaction: Tranfer request initiated and can be canceled before midnight. - Risk Score: 5

## This file contains high-risk transaction descriptions.
<br>Transaction: Immediate transfer request for $100,000 to a high-risk jurisdiction. - Risk Score: 9
<br>Transaction: Multiple wire transfers just under reporting threshold noticed. - Risk Score: 8
<br>Transaction: Payment to a company flagged for sanctions violations last month. - Risk Score: 8
<br>Transaction: Urgent cash disbursement request from an unrecognized offshore account. - Risk Score: 9
<br>Transaction: Suspicious invoice approval needed for payment exceeding $250,000. - Risk Score: 9

## This file contains low-risk transaction descriptions.
<br>Transaction: Monthly office rent payment via direct debit. - Risk Score: 1
<br>Transaction: Annual software license renewal fee. - Risk Score: 2
<br>Transaction: Regular payroll transaction for bi-weekly wages. - Risk Score: 1
<br>Transaction: Subscription fee payment for online services. - Risk Score: 3
<br>Transaction: Reimbursement for employee travel expenses. - Risk Score: 3


Process finished with exit code 0

## Conclusions
As we can see from the tests,
those statements that are intentionally risky all received a high score, and
those statements that are intentionally not risky all received a low score



