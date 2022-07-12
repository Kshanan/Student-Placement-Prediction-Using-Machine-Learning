# cr = 'create table register(id integer primary key autoincrement,uname varchar(12) unique,fname varchar(12),email varchar(20) unique,psw varchar(10),cpsw varchar(10))'
# cur.execute(cr)
# conn.commit()
# print('success')

# cr = 'create table quiz(id integer primary key autoincrement,date varchar(12),name varchar(10),c int,python int,java int,avg int)'
# cur.execute(cr)
# conn.commit()
# print('success')

# cur.execute('update Kshanan set python = 20  where date= "09/07/22" ')
# conn.commit()

# dis = 'select * from quiz'
# cur.execute(dis)
# print(cur.fetchall())
# avg_1 = cur.fetchall()
# print(avg_1)
# avg = avg_1[0][0] + avg_1[0][1] + avg_1[0][2] / 3
# avgg = round(avg)
# print(avgg)


# drp = 'drop table quiz'
# cur.execute(drp)
# conn.commit()
# print('Success')