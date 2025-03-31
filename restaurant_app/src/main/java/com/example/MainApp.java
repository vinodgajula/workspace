package com.example;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MainApp {
    public static void main(String[] args) {
        // Load the Spring Context using annotation-based configuration
        ApplicationContext context = new AnnotationConfigApplicationContext(RestaurantConfig.class);

        // Simulate a customer interacting with the restaurant
        RestaurantService restaurantService = context.getBean(RestaurantService.class);
        restaurantService.displayMenu();
        restaurantService.placeOrder("Pizza");
        restaurantService.placeOrder("Pasta");
        restaurantService.viewOrderHistory();

        FeedbackService feedbackService = context.getBean(FeedbackService.class);
        feedbackService.giveFeedback("The food was delicious!");
    }
}
