package com.example;

import org.springframework.stereotype.Service;

import java.util.Arrays;
import java.util.List;

@Service
public class MenuService {
    private final List<String> menuItems = Arrays.asList("Pizza", "Pasta", "Burger", "Salad");

    public List<String> getMenuItems() {
        return menuItems;
    }

    public boolean isDishAvailable(String dish) {
        return menuItems.contains(dish);
    }
}
