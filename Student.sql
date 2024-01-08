create table 學生資料表
(
學號 char(9),
姓名 nvarchar(50) not null,
性別 nvarchar(6) not null,
生日 nvarchar(100) not null,
班級編號 nvarchar(50) not null,
primary key(學號)
)
insert into 學生資料表
values('110B00001','小明','男','2006/02/28','資工A'),
('110B00002','大明','男','2005/05/24','資工C'),
('110B00003','小花','女','2005/03/10','資工B'),
('110B00004','大東','男','2006/01/12','資工B'),
('110B00005','凱琪','女','2006/02/11','資工A')
