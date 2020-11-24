package com.assistant.windfall.mbg.mapper;

import com.assistant.windfall.dao.TagDao;

import java.util.List;

public interface TagMapper {
    TagDao obtainTagById(Integer id);

    void insertTag(TagDao userDao);

    List<TagDao> listTag(Integer orgId);
}
