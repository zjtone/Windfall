package com.assistant.windfall.controller;

import java.util.List;

public interface InsertRefsHandler {
    void insert(Integer orgId, Integer id, List<Integer> refs);
}
