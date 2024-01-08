create table 教師資料表
(
教師編號 char(5),
姓名 nvarchar(50) not null,
primary key(教師編號)
)
insert into 教師資料表
values('S0001','威廉'),
('S0002','強森'),
('S0003','強尼'),
('S0004','保羅'),
('S0005','艾倫')
