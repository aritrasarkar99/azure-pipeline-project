--create schema awprojectSch

CREATE TABLE awprojectSch.customertbl
(
	customer_id INT,
	fullName VARCHAR(255),
	email VARCHAR(255),
	street VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(125),
	country VARCHAR(125)
);

select count(*) from awprojectSch.customertbl;

select * from awprojectSch.customertbl;




