package com.example;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

// Annotation-based configuration class
@Configuration
public class AppConfig {

    // Bean definition for GreetingService
    @Bean
    public GreetingService greetingService() {
        // Creating and configuring the GreetingService bean
        GreetingServiceImpl greetingService = new GreetingServiceImpl();
        greetingService.setGreetingMessage("Hello from Annotation Config!");
        return greetingService;
    }
}
