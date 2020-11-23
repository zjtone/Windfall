package com.assistant.windfall.dao;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public abstract class People extends Dao{
    protected Integer id;
    protected String username;
    protected String password;
    protected String idCard;
    protected String phone;
    protected String email;
    protected String openid;
    protected Integer orgId;
}
