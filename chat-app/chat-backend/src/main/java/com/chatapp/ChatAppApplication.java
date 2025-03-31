package com.chatapp;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.cassandra.repository.config.EnableCassandraRepositories;

@SpringBootApplication
@EnableCassandraRepositories  // ✅ Required for Cassandra repositories
public class ChatAppApplication {

    private static final Logger logger = LoggerFactory.getLogger(ChatAppApplication.class);

    public static void main(String[] args) {
        logger.info("Starting ChatAppApplication...");
        try {
            SpringApplication.run(ChatAppApplication.class, args);
            logger.info("ChatAppApplication started successfully.");
        } catch (Exception e) {
            logger.error("Application failed to start: {}", e.getMessage(), e);
            throw e;
        }
    }
}
