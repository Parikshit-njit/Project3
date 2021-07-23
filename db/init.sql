CREATE DATABASE addressData;
USE addressData;

CREATE TABLE IF NOT EXISTS addresses (
	`id` int AUTO_INCREMENT,
    `Fname` VARCHAR(21) CHARACTER SET utf8,
    `Lname` VARCHAR(8) CHARACTER SET utf8,
    `Address` VARCHAR(32) CHARACTER SET utf8,
    `City` VARCHAR(11) CHARACTER SET utf8,
    `State` VARCHAR(3) CHARACTER SET utf8,
    `Zip_Code` INT,
    primary key(`id`)
);
INSERT INTO addresses (Fname, Lname, Address, City, State, Zip_Code) VALUES
    ('John','Doe','120 jefferson st.','Riverside',' NJ',8075),
    ('Jack','McGinnis','220 hobo Av.','Phila',' PA',9119),
    ('John "Da Man"','Repici','120 Jefferson St.','Riverside',' NJ',8075),
    ('Stephen','Tyler','7452 Terrace "At the Plaza" road','SomeTown','SD',91234),
    (NULL,'Blankman',NULL,'SomeTown',' SD',298),
    ('Joan "the bone", Anne','Jet','9th, at Terrace plc','Desert City','CO',123);