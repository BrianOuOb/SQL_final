create table 使用者資料表
(
使用者編號 char(10),
帳號 char(9),
密碼 char(20),
身分 nvarchar(5) not null,
primary key(使用者編號)
)
insert into 使用者資料表
values('U1','110B00001','123456789','學生'),
('U2','S0003','0000','教師'),
('U3','GOD01','666','管理員')

