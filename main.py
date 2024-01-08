import pyodbc

# 連接到 SQL Server 数据库
server = 'DESKTOP-EH2GNVV\SQLSERVER2022'
database = 'MyeSchoolDB'
"""
server="localhost\SQLSERVER2019"
database="MyDBMS"
username="sa"
password="Cjcucsie0520"
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
"""
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
conn = pyodbc.connect(conn_str)

def Main_Menu():
    print('=====學生管理系統=====')
    print('1.學生資料')
    print('2.課程資料')
    print('3.班級資料')
    print('4.出席資料')
    print('5.成績資料')
    print('6.教師資料')
    print('7.使用者')
    n = eval(input('請選擇功能清單:'))
    if n == 1:
        Student_Manager()        
    elif n == 2:
        Course_Manger()
    elif n == 3:
        Class_Manger()
    elif n == 4:
        Attendance_Manger()
    elif n == 5:
        Grade_Manger()
    elif n == 6:
        Teacher_Manger()
    elif n == 7:
        Users_Manger()
# 學生資料
def Student_Manager():
    print('===學生資料===')
    print('1.新增學生資料')
    print('2.修改學生資料')
    print('3.刪除學生資料')
    print('4.查詢學生資料')
    print('5.回主畫面')
    n = eval(input('請選擇「學生」功能清單:'))
    if n == 1:
        Insert_Student()
    elif n == 2:
        Update_Student()
    elif n == 3:
        Delete_Student()
    elif n == 4:
        Query_Student()
    elif n == 5:
        Main_Menu()
    else:
        print('請選擇1~5項功能')    
def Check_Sid(Sid):
    SQLcmd = "select * from 學生資料表 where 學號 = '{}'".format(Sid)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()
def Insert_Student():
    Sid = input('學號')
    if Check_Sid(Sid)!=None:
        print('學號:{}重複了'.format(Sid))
        return
    Sname = input('姓名:')
    Sex = input('姓別:')
    date_of_birth = input('生日(西元年):')
    Class_id = input('班級編號:')
    SQLcmd = "INSERT INTO 學生資料表 VALUES ('{}', '{}', '{}', '{}', '{}')".format(Sid,Sname,Sex,date_of_birth,Class_id)
    conn.execute(SQLcmd)
    conn.commit()
    print('新增學生紀錄!')
    Student_Manager()
def Update_Student():
    Sid = input('學號')
    if Check_Sid(Sid)==None:
        print('查無此學號:{}'.format(Sid))
        return
    Sname = input('姓名:')
    Sex = input('姓別:')
    date_of_birth = input('生日(西元年):')
    Class_id = input('班級編號:')
    SQLcmd = "UPDATE 學生資料表 SET 姓名 = '{}', 性別 = '{}', 生日(西元年) = '{}',班級編號 = '{}'Where 學號 = '{}'".format(Sname,Sex,date_of_birth,Class_id,Sid)
    conn.execute(SQLcmd)
    conn.commit()
    print('更新學生紀錄!')
    Student_Manager()
def Delete_Student():
    Sid = input('學號:')
    if Check_Sid(Sid)==None:
        print('查無此學號:{}'.format(Sid))
        return
    SQLcmd = "DELETE FROM 學生資料表 WHERE 學號 = '{}'".format(Sid)
    conn.execute(SQLcmd)
    conn.commit()
    print('刪除紀錄成功!')
    Student_Manager()
def Query_Student():    
    SQLcmd = "SELECT * FROM 學生資料表"
    Record = conn.execute(SQLcmd)
    listStudent=list(Record.fetchall())
    print('   學號   姓名 性別 生日(西元年) 班級編號')
    for row in listStudent:
        for col in row:
            print(col, end="  ")
        print()
    Record.close()        
    Student_Manager()
#課程資料
def Course_Manger():
    print('===課程資料===')
    print('1.新增課程資料')
    print('2.修改課程資料')
    print('3.刪除課程資料')
    print('4.查詢課程資料')
    print('5.回主畫面')
    n = eval(input('請選擇「課程」功能清單:'))
    if n == 1:
        Insert_Course()
    elif n == 2:
        Update_Course()
    elif n == 3:
        Delete_Course()
    elif n == 4:
        Query_Course()
    elif n == 5:
        Main_Menu()
    else:
        print('請選擇1~5項功能')    
def Check_Course_id(Course_id):
    SQLcmd = "select * from 課程資料表 where 課程編號 = '{}'".format(Course_id)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()
def Insert_Course():
    Course_id = input('課程編號')
    if Check_Course_id(Course_id)!=None:
        print('課程編號:{}重複了'.format(Course_id))
        return
    Course_name = input('課程名稱:')
    Tid = input('教師編號:')
    Ctime = input('上課時間:')
    Class_location = input('上課地點:')
    Credit = input('學分:')
    SQLcmd = "INSERT INTO 課程資料表 VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(Course_id,Course_name,Tid,Ctime,Class_location,Credit)
    conn.execute(SQLcmd)
    conn.commit()
    print('新增課程紀錄!')
    Course_Manger()
def Update_Course():
    Course_id = input('課程編號')
    if Check_Course_id(Course_id)==None:
        print('查無此課程:{}'.format(Course_id))
        return
    Course_name = input('課程名稱:')
    Tid = input('教師編號:')
    Ctime = input('上課時間:')
    Class_location = input('上課地點:')
    Credit = input('學分:')
    SQLcmd = "UPDATE 課程資料表 SET 課程名稱 = '{}', 教師編號 = '{}', 上課時間 = '{}',上課地點 = '{}',學分 = '{}'Where 課程編號 = '{}'".format(Course_name,Tid,Ctime,Class_location,Credit,Course_id)
    conn.execute(SQLcmd)
    conn.commit()
    print('更新課程紀錄!')
    Course_Manger()
def Delete_Course():
    Course_id = input('課程編號')
    if Check_Course_id(Course_id)==None:
        print('查無此課程:{}'.format(Course_id))
        return
    SQLcmd = "DELETE FROM 課程資料表 WHERE 課程編號 = '{}'".format(Course_id)
    conn.execute(SQLcmd)
    conn.commit()
    print('刪除紀錄成功!')
    Course_Manger()
def Query_Course():    
    SQLcmd = "SELECT * FROM 課程資料表"
    Record = conn.execute(SQLcmd)
    listCourse=list(Record.fetchall())
    print('課程編號 課程名稱   教師編號 上課時間 上課地點 學分')
    for row in listCourse:
        for col in row:
            print(col, end="  ")
        print()
    Record.close()        
    Course_Manger()
#班級資料 
def Class_Manger():
    print('===班級資料===')
    print('1.修改班級資料')
    print('2.刪除班級資料')
    print('3.查詢班級資料')
    print('4.回主畫面')
    n = eval(input('請選擇「班級」功能清單:'))
    if n == 1:
        Update_Class()
    elif n == 2:
        Delete_Class()
    elif n == 3:
        Query_Class()
    elif n == 4:
        Main_Menu()
    else:
        print('請選擇1~4項功能')
def Check_Class_id(Class_id):
    SQLcmd = "select * from 班級資料表 where 班級編號 = '{}'".format(Class_id)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()            
def Update_Class():
    Class_id = input('班級編號')
    if Check_Class_id(Class_id)==None:
        print('查無此班級:{}'.format(Class_id))
        return
    Tutor_id = input('班主任編號:')  
    Sid = input('班級成員編號:')    
    SQLcmd = "UPDATE 班級資料表 SET 班級編號 = '{}', 班主任編號 = '{}', 班級成員編號 = '{}'".format(Tutor_id,Sid,Class_id)
    conn.execute(SQLcmd)
    conn.commit()
    print('更新班級資料成功!')
    Class_Manger()
def Delete_Class():
    Class_id = input('班級編號')
    if Check_Class_id(Class_id)==None:
        print('查無此班級:{}'.format(Class_id))
        return    
    SQLcmd = "DELETE FROM 班級資料表 WHERE 班級編號 = '{}'".format(Class_id)
    conn.execute(SQLcmd)
    conn.commit()
    print('刪除成功!')
    Class_Manger()
def Query_Class():    
    SQLcmd = "SELECT * FROM 班級資料表"
    Record = conn.execute(SQLcmd)
    listClass=list(Record.fetchall())
    print('班級編號 班主任編號 班級成員編號')
    for row in listClass:
        for col in row:
            print(col, end="    ")
        print()
    Record.close()        
    Class_Manger()       
#出席資料
def Attendance_Manger():
    print('===出席資料===')
    print('1.新增出席資料')
    print('2.修改出席資料')
    print('3.刪除出席資料')
    print('4.查詢查詢資料')
    print('5.回主畫面')
    n = eval(input('請選擇「出席」功能清單:'))
    if n == 1:
        Insert_Attendance()
    elif n == 2:
        Update_Attendance()
    elif n == 3:
        Delete_Attendance()
    elif n == 4:
        Query_Attendance()
    elif n == 5:
        Main_Menu()
    else:
        print('請選擇1~5項功能')    
def Insert_Attendance():
    Aid = input('出席記錄編號:')    
    Sid = input('學號:')
    Class_id = input('班級編號:')
    Sname = input('姓名:')
    Time = input('點名時間:')
    Attendance_status = input('出席狀態:')
    Remark = input('備註:')
    SQLcmd = "INSERT INTO 出席資料表 VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Aid,Sid,Class_id,Sname,Time,Attendance_status,Remark)
    conn.execute(SQLcmd)
    conn.commit()
    print('新增出席紀錄!')
    Attendance_Manger()
def Update_Attendance():
    Aid = input('出席記錄編號:')    
    Sid = input('學號:')
    Class_id = input('班級編號:')
    Sname = input('姓名:')
    Time = input('點名時間:')
    Attendance_status = input('出席狀態:')
    Remark = input('備註:')    
    SQLcmd = "UPDATE 出席資料表 SET 學號 = '{}', 班級編號 = '{}', 姓名 = '{}',點名時間 = '{}',出席狀態 = '{}',備註 = '{}'Where 出席記錄編號 = '{}'".format(Sid,Class_id,Sname,Time,Attendance_status,Remark,Aid)
    conn.execute(SQLcmd)
    conn.commit()
    print('更新出席紀錄!')
    Attendance_Manger()
def Delete_Attendance():
    Aid = input('出席記錄編號:')   
    SQLcmd = "DELETE FROM 出席資料表 WHERE 出席紀錄編號 = '{}'".format(Aid)
    conn.execute(SQLcmd)
    conn.commit()
    print('刪除紀錄成功!')
    Attendance_Manger()
def Query_Attendance():    
    SQLcmd = "SELECT * FROM 出席資料表"
    Record = conn.execute(SQLcmd)
    listAttendance=list(Record.fetchall())
    print('出席紀錄編號 學號 班級編號 課程編號 點名時間 出席狀態 備註')
    for row in listAttendance:
        for col in row:
            print(col, end=" ")
        print()
    Record.close()        
    Attendance_Manger()
#成績資料
def Grade_Manger():
    print('===成績資料===')
    print('1.新增成績資料')
    print('2.修改成績資料')
    print('3.刪除成績資料')
    print('4.查詢成績資料')
    print('5.回主畫面')
    n = eval(input('請選擇「成績」功能清單:'))
    if n == 1:
        Insert_Grade()
    elif n == 2:
        Update_Grade()
    elif n == 3:
        Delete_Grade()
    elif n == 4:
        Query_Grade()
    elif n == 5:
        Main_Menu()
    else:
        print('請選擇1~5項功能')    
def Insert_Grade():
    Sid = input('學號')
    Course_id = input('課程編號:')
    Grade = input('成績:')
    SQLcmd = "INSERT INTO 成績資料表 VALUES ('{}', '{}', '{}')".format(Sid,Course_id,Grade)
    conn.execute(SQLcmd)
    conn.commit()
    print('新增成績紀錄!')
    Grade_Manger()
def Update_Grade():
    Sid = input('學號')   
    Course_id = input('課程編號:')
    Grade = input('成績:')    
    SQLcmd = "UPDATE 成績資料表 SET 課程編號 = '{}', 成績 = '{}'Where 學號 = '{}'".format(Course_id,Grade,Sid)
    conn.execute(SQLcmd)
    conn.commit()
    print('更新成績紀錄!')
    Grade_Manger()
def Delete_Grade():
    Sid = input('學號:')    
    SQLcmd = "DELETE FROM 成績資料表 WHERE 學號 = '{}'".format(Sid)
    conn.execute(SQLcmd)
    conn.commit()
    print('刪除成績成功!')
    Grade_Manger()
def Query_Grade():    
    SQLcmd = "SELECT * FROM 成績資料表"
    Record = conn.execute(SQLcmd)
    listGrade=list(Record.fetchall())
    print('  學號   課程編號 成績')
    for row in listGrade:
        for col in row:
            print(col, end="  ")
        print()
    Record.close()        
    Grade_Manger()
#教師資料
def Teacher_Manger():
    print('===教師資料===')
    print('1.新增教師資料')
    print('2.修改教師資料')
    print('3.刪除教師資料')
    print('4.查詢教師資料')
    print('5.回主畫面')
    n = eval(input('請選擇「教師」功能清單:'))
    if n == 1:
        Insert_Teacher()
    elif n == 2:
        Update_Teacher()
    elif n == 3:
        Delete_Teacher()
    elif n == 4:
        Query_Teacher()
    elif n == 5:
        Main_Menu()
    else:
        print('請選擇1~5項功能')    
def Check_Tid(Tid):
    SQLcmd = "select * from 教師資料表 where 教師編號 = '{}'".format(Tid)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()
def Insert_Teacher():
    Tid = input('教師編號:')
    if Check_Tid(Tid)!=None:
        print('教師編號:{}重複了'.format(Tid))
        return
    Tname = input('姓名:')    
    SQLcmd = "INSERT INTO 教師資料表 VALUES ('{}', '{}')".format(Tid,Tname,)
    conn.execute(SQLcmd)
    conn.commit()
    print('新增紀錄成功!')
    Teacher_Manger()
def Update_Teacher():
    Tid = input('教師編號:')
    if Check_Tid(Tid)==None:
        print('查無此教師:{}'.format(Tid))
        return
    Tname = input('姓名:')    
    SQLcmd = "UPDATE 教師資料表 SET 姓名 = '{}'Where 教師編號 = '{}'".format(Tname,Tid)
    conn.execute(SQLcmd)
    conn.commit()
    print('更新資料成功!')
    Teacher_Manger()
def Delete_Teacher():
    Tid = input('教師編號:')
    if Check_Tid(Tid)==None:
        print('查無此教師:{}'.format(Tid))
        return
    SQLcmd = "DELETE FROM 教師資料表 WHERE 教師編號 = '{}'".format(Tid)
    conn.execute(SQLcmd)
    conn.commit()
    print('刪除紀錄成功!')
    Teacher_Manger()
def Query_Teacher():    
    SQLcmd = "SELECT * FROM 教師資料表"
    Record = conn.execute(SQLcmd)
    listTeacher=list(Record.fetchall())
    print('教師編號 姓名')
    for row in listTeacher:
        for col in row:
            print(col, end="  ")
        print()
    Record.close()        
    Teacher_Manger()
#使用者
def Users_Manger():
    print('===使用者資料===')
    print('1.新增使用者資料')
    print('2.修改使用者資料')
    print('3.刪除使用者資料')
    print('4.查詢使用者資料')
    print('5.回主畫面')
    n = eval(input('請選擇「使用者」功能清單:'))
    if n == 1:
        Insert_Users()
    elif n == 2:
        Update_Users()
    elif n == 3:
        Delete_Users()
    elif n == 4:
        Query_Users()
    elif n == 5:
        Main_Menu()
    else:
        print('請選擇1~5項功能')    
def Check_Uid(Uid):
    SQLcmd = "select * from 使用者資料表 where 使用者編號 = '{}'".format(Uid)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()
def Insert_Users():
    Uid = input('使用者編號:')
    if Check_Uid(Uid)!=None:
        print('使用者編號:{}重複了'.format(Uid))
        return
    Uname = input('帳號:')
    Ucode = input('密碼:')
    U_identity = input('身分:')    
    SQLcmd = "INSERT INTO 使用者資料表 VALUES ('{}', '{}', '{}', '{}')".format(Uid,Uname,Ucode,U_identity)
    conn.execute(SQLcmd)
    conn.commit()
    print('新增紀錄成功!')
    Users_Manger()
def Update_Users():
    Uid = input('使用者編號:')
    if Check_Uid(Uid)==None:
        print('查無此使用者:{}'.format(Uid))
        return
    Uname = input('帳號:')
    Ucode = input('密碼:')
    U_identity = input('身分:')     
    SQLcmd = "UPDATE 使用者資料表 SET 帳號 = '{}', 密碼 = '{}', 身分 = '{}' Where 使用者編號 = '{}'".format(Uname,Ucode,U_identity,Uid)
    conn.execute(SQLcmd)
    conn.commit()
    print('更新資料成功!')
    Users_Manger()
def Delete_Users():
    Uid = input('使用者編號:')
    if Check_Uid(Uid)==None:
        print('查無此使用者:{}'.format(Uid))
        return
    SQLcmd = "DELETE FROM 使用者資料表 WHERE 使用者編號 = '{}'".format(Uid)
    conn.execute(SQLcmd)
    conn.commit()
    print('刪除紀錄成功!')
    Users_Manger()
def Query_Users():    
    SQLcmd = "SELECT * FROM 使用者資料表"
    Record = conn.execute(SQLcmd)
    listUsers=list(Record.fetchall())
    print('使用者編號 帳號      密碼                 身分')
    for row in listUsers:
        for col in row:
            print(col, end=" ")
        print()
    Record.close()        
    Users_Manger()            
while True:
    Main_Menu()
conn.close()
































