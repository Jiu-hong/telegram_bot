## STEP1:

### prepare requirements 

`pip install -r requirements.txt`


## STEP2:
Issue command in script file. 

### For test
cat chatids_test | cut -f1 -d ' ' > chatids
### For production
cat chatids_product | cut -f1 -d ' ' > chatids


## STEP3:

python main.py


