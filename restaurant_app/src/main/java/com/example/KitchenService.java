package com.example;

import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

@Service
public class KitchenService {
    @PostConstruct
    public void init() {
        System.out.println("Kitchen is now ready for preparing dishes.");
    }

    public void prepareDish(String dish) {
        System.out.println("Preparing: " + dish);
        System.out.println(dish + " is ready to be served!");
    }

    @PreDestroy
    public void shutdown() {
        System.out.println("Kitchen is closing down. Goodbye!");
    }
}
