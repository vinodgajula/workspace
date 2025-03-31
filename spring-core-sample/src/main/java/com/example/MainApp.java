package com.example;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MainApp {
    public static void main(String[] args) {
        // Using XML Configuration to load the Spring Context
        //System.out.println("Using XML Configuration:");
        //ApplicationContext xmlContext = new ClassPathXmlApplicationContext("META-INF/beans.xml");

        // Retrieve the GreetingService bean by its ID and invoke its method
        //GreetingService xmlGreetingService = (GreetingService) xmlContext.getBean("greetingService");
        //xmlGreetingService.sayGreeting();

        // Close the XML-based context to demonstrate bean destruction
        //((ClassPathXmlApplicationContext) xmlContext).close();

        // Using Annotation Configuration to load the Spring Context
        System.out.println("\nUsing Annotation Configuration:");
        ApplicationContext annotationContext = new AnnotationConfigApplicationContext(AppConfig.class);

        // Retrieve the GreetingService bean by its type and invoke its method
        GreetingService annotationGreetingService = annotationContext.getBean(GreetingService.class);
        annotationGreetingService.sayGreeting();

        // Close the Annotation-based context
        ((AnnotationConfigApplicationContext) annotationContext).close();
    }
}
