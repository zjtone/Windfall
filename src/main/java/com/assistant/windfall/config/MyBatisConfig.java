package com.assistant.windfall.config;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@MapperScan("com.assistant.windfall.mbg.mapper")
public class MyBatisConfig {
}
