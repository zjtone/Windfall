CREATE TABLE MyUser (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `img` VARCHAR(250),
    `username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `parentId` bigint(20) DEFAULT -1,
    `idCard` VARCHAR(20),
    `phone` VARCHAR(20),
    `email` VARCHAR(100),
    `openid` VARCHAR(256),
    `orgId` int,
    `status` int DEFAULT 1,
    `create_time` DATE,
    `update_time` DATE,
    `delete_time` DATE
);

CREATE TABLE Organization (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50),
    `email` VARCHAR(20) NOT NULL UNIQUE,
    `password` VARCHAR(20) NOT NULL,
    `description` VARCHAR(512),
    `status` int DEFAULT 1,
    `orgId` int,
    `create_time` DATE,
    `update_time` DATE,
    `delete_time` DATE
);

CREATE TABLE Course (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50),
    `img` VARCHAR(250),
    `description` VARCHAR(512),
    `status` int DEFAULT 1,
    `orgId` int
);

CREATE TABLE Employee (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `idCard` VARCHAR(20),
    `phone` VARCHAR(20),
    `email` VARCHAR(100),
    `openid` VARCHAR(256),
    `orgId` int,
    `status` int DEFAULT 1,
    `create_time` DATE,
    `update_time` DATE,
    `delete_time` DATE
);

CREATE TABLE Teacher (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `idCard` VARCHAR(20),
    `phone` VARCHAR(20),
    `email` VARCHAR(100),
    `openid` VARCHAR(256),
    `orgId` int,
    `status` int DEFAULT 1,
    `create_time` DATE,
    `update_time` DATE,
    `delete_time` DATE
);

CREATE TABLE Tag (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    `status` int DEFAULT 1,
    `orgId` int,
    `create_time` DATE,
    `update_time` DATE,
    `delete_time` DATE
);

CREATE TABLE CourseTagRef (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `courseId` bigint(20),
    `tagId` bigint(20),
    `status` int DEFAULT 1,
    `orgId` int,
    `create_time` DATE,
    `update_time` DATE,
    `delete_time` DATE
);

CREATE TABLE CourseTeacherRef (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `courseId` bigint(20),
    `teacherId` bigint(20),
    `status` int DEFAULT 1,
    `orgId` int,
    `create_time` DATE,
    `update_time` DATE,
    `delete_time` DATE
);
