#HW02_2
import random

stu_list = {'S'+ str(x) for x in range(1,51)}
compute_stu_list = {'S'+ str(i) for i in  random.sample(range(1,51),10)}
guitar_stu_list = {'S'+ str(i) for i in  random.sample(range(1,51),10)}

print("學生列表："+str(stu_list))
print("參與電腦社的學生："+str(compute_stu_list))
print("參與吉他社的學生："+str(guitar_stu_list))
print("都有參加的學生："+str(compute_stu_list & guitar_stu_list))
print("只參加電腦社的學生："+str(compute_stu_list - guitar_stu_list) )
print("只參加吉他社的學生："+str(guitar_stu_list - compute_stu_list))
print("都沒有參加的學生："+str(stu_list-(compute_stu_list | guitar_stu_list)))



