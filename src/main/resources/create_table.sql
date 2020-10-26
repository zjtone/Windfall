CREATE TABLE MyUser (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `type` int DEFAULT(1),
    `idCard` VARCHAR(20),
    `phone` VARCHAR(20),
    `email` VARCHAR(100),
    `openid` VARCHAR(256),
    `orgId` int
);