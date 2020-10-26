package com.assistant.windfall.service;

import com.assistant.windfall.dao.OrgDao;
import com.assistant.windfall.dao.UserDao;
import com.assistant.windfall.mbg.mapper.OrgMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class OrgService {
    @Autowired
    OrgMapper orgMapper;

    public OrgDao obtainOrgById(Integer id){
        return orgMapper.obtainOrgById(id);
    }

    public void insertOrg(OrgDao orgDao){
        orgMapper.insertOrg(orgDao);
    }
}
