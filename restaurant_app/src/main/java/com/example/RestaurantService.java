package com.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class RestaurantService {
    private final KitchenService kitchenService;
    private final MenuService menuService;
    private final List<String> orderHistory = new ArrayList<>();

    @Autowired
    public RestaurantService(KitchenService kitchenService, MenuService menuService) {
        this.kitchenService = kitchenService;
        this.menuService = menuService;
    }

    public void displayMenu() {
        System.out.println("Menu:");
        menuService.getMenuItems().forEach(System.out::println);
    }

    public void placeOrder(String dish) {
        if (menuService.isDishAvailable(dish)) {
            System.out.println("Order received for: " + dish);
            kitchenService.prepareDish(dish);
            orderHistory.add(dish);
        } else {
            System.out.println("Sorry, " + dish + " is not available.");
        }
    }

    public void viewOrderHistory() {
        System.out.println("Order History:");
        orderHistory.forEach(System.out::println);
    }
}
