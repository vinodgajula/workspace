package com.example;

import org.springframework.stereotype.Service;

@Service
public class FeedbackService {
    public void giveFeedback(String feedback) {
        System.out.println("Customer Feedback: " + feedback);
    }
}
