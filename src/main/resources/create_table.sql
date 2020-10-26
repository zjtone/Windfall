CREATE TABLE MyUser (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `type` int DEFAULT(1),
    `idCard` VARCHAR(20),
    `phone` VARCHAR(20),
    `email` VARCHAR(100),
    `openid` VARCHAR(256),
    `orgId` int,
    `status` int DEFAULT(1),
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
    `status` int DEFAULT(1),
    `create_time` DATE,
    `update_time` DATE,
    `delete_time` DATE
);
