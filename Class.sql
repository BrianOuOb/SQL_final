create table �Z�Ÿ�ƪ�
(
�Z�Žs�� nvarchar(50) not null,
�Z�D���s�� char(5),
�Z�Ŧ����Ǹ� char(9),
primary key(�Z�D���s��,�Z�Ŧ����Ǹ�),
foreign key(�Z�D���s��)references �Юv��ƪ�(�Юv�s��)
on update cascade
on delete cascade,
foreign key(�Z�Ŧ����Ǹ�)references �ǥ͸�ƪ�(�Ǹ�),
)
insert into �Z�Ÿ�ƪ�
values('��uA','S0001','110B00001'),
('��uA','S0001','110B00005'),
('��uB','S0002','110B00003'),
('��uB','S0002','110B00004'),
('��uC','S0003','110B00002')

