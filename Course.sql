create table 課程資料表
(
課程編號 char(5),
課程名稱 nvarchar(10) not null,
教師編號 char(5),
上課時間 nvarchar(100) not null,
上課地點 nvarchar(6) not null,
學分 int,
primary key(課程編號)
)

insert into 課程資料表
values('ACS01','作業系統','S0001','Tuesday:9:10~12:00','T20406','3'),
('ACS02','系統程式','S0002','Thursday:9:10~12:00','T30102','3'),
('ACS03','系統分析與設計','S0003','Wednesday:13:20~16:10','L20101','3'),
('ACS04','大數據資料分析','S0004','Thursday:13:20~16:10','L20102','3'),
('ACS05','資料庫系統','S0005','Monday:9:10~12:00','L2B102','3')
