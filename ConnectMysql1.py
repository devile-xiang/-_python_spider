#endoding:utf-8


import pymysql
import re
import time

def main():
    codatalist = []
    for i in range(3):
        couser1 = {
            "公司名": "渭南人力资源有限公司%d" % i,
            '公司法人': "为祥和%d" % i,
            '公司电话': "1855555555%d" % i,
            '公司邮箱': "290463340%d@qq.com" % i,
            '公司地址': "渭南市%d" % i,
            '公司状态': "开业%d" % i,
            '公司资金': "500%d万" % i,
            '公司成立日期': "2018年12月1%d" % i,
        }
        codatalist.append(couser1)
    db = pymysql.connect("localhost", "root", "", "crm_qh0913_com")
    cursor=db.cursor()

    sqlmax="select max(customer_id) from jx_customer"
    cursor.execute(sqlmax)
    maxnum=cursor.fetchone()
    print(maxnum[0])



    for i,data1 in enumerate(codatalist):
        # try:
        i=i+1+maxnum[0]
        sql="select * from jx_customer where name='%s'"%data1['公司名']
        cursor.execute(sql)
        results=cursor.fetchall()
        ticks = time.time()
        ticks=int(ticks)
        if len(results)==0:
            sql1='INSERT INTO jx_customer'\
                 '(customer_id,owner_role_id,creator_role_id,' \
                 'contacts_id,name,' \
                 'origin,address,' \
                 'zip_code,industry,' \
                 'annual_revenue,ownership,' \
                 'rating,create_time,' \
                 'update_time,is_deleted,' \
                 'is_locked,delete_time,' \
                 'delete_role_id) values (%d,%d,%d,%d,"%s","","%s","","","","","",%d,0,0,0,0,0)'%\
                 (i,0,1,1,data1['公司名'],data1['公司地址'],ticks)
            print(sql1)
            cursor.execute(sql1)
            db.commit()
            sql2='INSERT into jx_contacts(contacts_id,creator_role_id,name,post,department,sex,saltname,telephone,email,qq_no,address,zip_code,description,create_time,update_time,is_deleted,delete_role_id,delete_time)' \
                'values (%d,2,"%s","法人","无",0,"未知","%s","%s","","","","","%s","%s",0,0,0)'%(i,data1['公司法人'],data1['公司电话'],data1['公司邮箱'],ticks,ticks)
            print(sql2)
            cursor.execute(sql2)
            db.commit()
            sql3 = 'INSERT into jx_customer_data(customer_id,description)' \
                   'values (%d,"%s")'%(i,data1['公司状态']+'----------'+data1['公司资金']+'----------'+data1['公司成立日期'])
            print(sql3)
            cursor.execute(sql3)
            db.commit()
            print("成功插入数据")
        else:
            print("数据库存在此数据")
            print(results[0][0])
            id=results[0][0]
            id=int(id)
            print(id)
            # "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
            # sql1 = 'INSERT INTO jx_customer' \
            #        '(customer_id,owner_role_id,creator_role_id,' \
            #        'contacts_id,name,' \
            #        'origin,address,' \
            #        'zip_code,industry,' \
            #        'annual_revenue,ownership,' \
            #        'rating,create_time,' \
            #        'update_time,is_deleted,' \
            #        'is_locked,delete_time,' \
            #        'delete_role_id) values (%d,%d,%d,%d,"%s","","%s","","","","","",%d,0,0,0,0,0)' % \
            #        (i, 0, 1, 1, data1['公司名'], data1['公司地址'], ticks)
            # print(sql1)
            # cursor.execute(sql1)
            # db.commit()
            sql4 = 'UPDATE jx_contacts set name="%s" , telephone="%s" , email="%s" , update_time="%s" where contacts_id=%d'\
                   %(data1['公司法人'], data1['公司电话'], data1['公司邮箱'], ticks,id)
            print(sql4)
            cursor.execute(sql4)
            db.commit()
            # sql3 = 'INSERT into jx_customer_data(customer_id,description)' \
            #        'values (%d,"%s")' % (
            #        i, data1['公司状态'] + '----------' + data1['公司资金'] + '----------' + data1['公司成立日期'])
            # print(sql3)
            # cursor.execute(sql3)
            # db.commit()
            print("成功更新数据")





        # except Exception:
        #     # print(sql2)
        #     print(Exception)
        #     # print(results)
        #
        #     print("数据库操作出现错误")
        #     db.rollback()
    db.close()









if __name__ == '__main__':
    main()