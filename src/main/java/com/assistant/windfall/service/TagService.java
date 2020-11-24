package com.assistant.windfall.service;

import com.assistant.windfall.dao.TagDao;
import com.assistant.windfall.mbg.mapper.TagMapper;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TagService {
    @Autowired
    TagMapper tagMapper;

    public TagDao obtainTagById(Integer id){
        return tagMapper.obtainTagById(id);
    }

    public void insertTag(TagDao TagDao){
        tagMapper.insertTag(TagDao);
    }

    public List<TagDao> listTag(int pageNum, int pageSize, Integer orgId) {
        PageHelper.startPage(pageNum, pageSize);
        return tagMapper.listTag(orgId);
    }
}
