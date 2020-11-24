package com.assistant.windfall.service;

import com.assistant.windfall.dao.EmployeeDao;
import com.assistant.windfall.dao.OrgDao;
import com.assistant.windfall.dao.UserDao;
import com.assistant.windfall.mbg.mapper.OrgMapper;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class OrgService {
    @Autowired
    OrgMapper orgMapper;

    public OrgDao obtainOrgById(Integer id) {
        return orgMapper.obtainOrgById(id);
    }

    public void insertOrg(OrgDao orgDao) {
        orgMapper.insertOrg(orgDao);
    }

    public List<EmployeeDao> listOrg(Integer pageNum, Integer pageSize, Integer orgId) {
        PageHelper.startPage(pageNum, pageSize);
        return orgMapper.listOrg(orgId);
    }
}
