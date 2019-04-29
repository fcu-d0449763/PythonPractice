#HW03_02
import csv
def rowsoucedate(row):
    print(row['民調來源'],end='\t ')
    print(row['完成日期'],end='\t ')
    
def rowkey(cdd,row):
    for x in cdd:
        for k in row.keys():
            if k.endswith(x):
                print(row[k],end='\t ')
    print('')

def poll(org, *cdd):
    with open('vote.csv', newline='' , encoding = 'utf8') as csvfile:
        rows = csv.DictReader(csvfile)
        if cdd:
            print('民調來源\t','完成日期\t',end=' ')
            for x in cdd:
                print(x,end='\t ')
            print()
        else:
            print('民調來源\t','完成日期\t','柯文哲\t','丁守中\t','姚文智')

        for row in rows:
            tmp = ('柯文哲','丁守中','姚文智')
            if isinstance(org,tuple):
                for i in org:
                    if row['民調來源'] == i :
                        rowsoucedate(row)
                        if cdd:
                            rowkey(cdd,row)
                        else:
                            rowkey(tmp,row)
            else:
                if row['民調來源'] == org :
                    rowsoucedate(row)
                    if cdd:
                        rowkey(cdd,row)
                    else:
                        rowkey(tmp,row)
                    
                    
m = ('TVBS','三立','美麗島')
poll(m,'姚文智','丁守中')
poll(('Yahoo'))
poll(('三立'))
poll(('TVBS'),'姚文智','丁守中')
poll(('TVBS'),'姚文智','柯文哲')