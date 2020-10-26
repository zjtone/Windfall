package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.OrgDao;

public interface OrgMapper {
    OrgDao obtainOrgById(Integer id);

    void insertOrg(OrgDao userDao);
}
