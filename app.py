import streamlit as st
import pickle

st.title('Bank Loan Prediction System')

model=pickle.load(open('logistic_regression_model.pkl','rb'))

##Accoutn NO
account_no=st.text_input('Account_number')

#full name
fn=st.text_input('Full Name')

#for gender
gen_display=('Female','Male')
gen_options=list(range(len(gen_display)))
gen=st.selectbox('Gender',gen_options,format_func=lambda x:gen_display[x])

#for marital status
mar_display=('No','Yes')
mar_options=list(range(len(mar_display)))
mar=st.selectbox('Marital Status',mar_options,format_func=lambda x:mar_display[x])

#no of dependents
dep_display=('No','One','Two','More than Two')
dep_options=list(range(len(dep_display)))
dep=st.selectbox('Dependents',dep_options,format_func=lambda x:dep_display[x])

#for education
edu_display=('Not Graduate','Graduate')
edu_options=list(range(len(edu_display)))
edu=st.selectbox('Education',edu_options,format_func=lambda x:edu_display[x])

#for emp status
emp_display=('Job','Business')
emp_options=list(range(len(emp_display)))
emp=st.selectbox('Employment Status',emp_options,format_func=lambda x:emp_display[x])

#for  property status
prop_display=('Rural','Semi-Urban','Urban')
prop_options=list(range(len(prop_display)))
prop=st.selectbox('Property Area',prop_options,format_func=lambda x:prop_display[x])

#for credit score
cred_display=('Between 300 to 500','Above 500')
cred_options=list(range(len(cred_display)))
cred=st.selectbox('Credit Score',cred_options,format_func=lambda x:cred_display[x])


#Applicants monthly income
mon_income=st.number_input("Applicant's Monthly Income($)",value=0)

#Co Applicant Monthly Income
co_mon_income=st.number_input("co-applicant's monthly income($)",value=0)

##Loan Amount
loan_amt=st.number_input('Loan Amount',value=0)

#loan duration
dur_display=['2 month','6 month','8 month','1 year','16 month']
dur_options=list(range(len(dur_display)))
dur=st.selectbox('Duration',dur_options,format_func=lambda x:dur_display[x])

if st.button('Submit'):
    duration=0
    if dur==0:
        duration=60
    if dur==1:
        duration=180
    if dur==2:
        duration=240

    if dur==3:
        duration=360
    if dur==4:
        duration=480


features=[[gen,mar,dep,edu,emp,mon_income,co_mon_income,loan_amt,dur,cred,prop]]
print(features)
prediction=model.predict(features)
lc=[str(i) for i in prediction]

ans=int(''.join(lc))

if ans==0:
    st.error(
        'Hello: '+fn +"||"
        'According to out calculations,you will not get the loan from bank'
    )

else:
    st.success(
        'Hello:' + fn +"||"
        'Account Number:' +account_no+ '||'
        'According to our calculations, you will get the loan from bank'
    )    