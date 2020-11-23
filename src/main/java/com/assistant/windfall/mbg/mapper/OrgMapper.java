package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.EmployeeDao;
import com.assistant.windfall.dao.OrgDao;

import java.util.List;

public interface OrgMapper {
    OrgDao obtainOrgById(Integer id);

    void insertOrg(OrgDao orgDao);

    List<EmployeeDao> listOrg();
}
