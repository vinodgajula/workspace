package com.example;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

// Implementation of the GreetingService interface
public class GreetingServiceImpl implements GreetingService {
    private String greetingMessage;

    // Default Constructor
    public GreetingServiceImpl() {
        System.out.println("GreetingServiceImpl: Inside Constructor");
    }

    // Setter for dependency injection
    public void setGreetingMessage(String greetingMessage) {
        this.greetingMessage = greetingMessage;
    }

    // Method to print the greeting message
    @Override
    public void sayGreeting() {
        System.out.println(greetingMessage);
    }

    // Lifecycle callback invoked after bean initialization
    @PostConstruct
    public void init() {
        System.out.println("GreetingServiceImpl: Inside @PostConstruct - Initialization logic here");
    }

    // Lifecycle callback invoked before bean destruction
    @PreDestroy
    public void destroy() {
        System.out.println("GreetingServiceImpl: Inside @PreDestroy - Cleanup logic here");
    }
}
