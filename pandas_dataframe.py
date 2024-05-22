import pandas as pd

def createDataframe(student_data):
    out = pd.DataFrame(student_data,columns=['student_id','age'])
    return out


student_data=[[1,15],[2,11],[3,11],[4,20]]