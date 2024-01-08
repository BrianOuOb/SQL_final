create table 班級資料表
(
班級編號 nvarchar(50) not null,
班主任編號 char(5),
班級成員學號 char(9),
primary key(班主任編號,班級成員學號),
foreign key(班主任編號)references 教師資料表(教師編號)
on update cascade
on delete cascade,
foreign key(班級成員學號)references 學生資料表(學號),
)
insert into 班級資料表
values('資工A','S0001','110B00001'),
('資工A','S0001','110B00005'),
('資工B','S0002','110B00003'),
('資工B','S0002','110B00004'),
('資工C','S0003','110B00002')

