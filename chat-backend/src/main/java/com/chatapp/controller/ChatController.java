package com.chatapp.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.chatapp.model.Message;
import com.chatapp.service.MessageService;

@RestController
@RequestMapping("/chat")
public class ChatController {

    private static final Logger logger = LoggerFactory.getLogger(ChatController.class);

    @Autowired
    private MessageService messageService;

    @PostMapping("/send")
    public ResponseEntity<String> sendMessage(@RequestBody Message message) {
        logger.info("Sending message from '{}' to '{}'", message.getSender(), message.getReceiver());

        try {
            messageService.sendMessage(message);
            logger.info("Message sent successfully");
            return ResponseEntity.ok("Message Sent!");
        } catch (Exception e) {
            logger.error("Failed to send message: {}", e.getMessage(), e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Failed to send message.");
        }
    }

    @GetMapping("/messages")
    public ResponseEntity<List<Message>> getMessages(@RequestParam String user1, @RequestParam String user2) {
        logger.info("Fetching messages between '{}' and '{}'", user1, user2);

        try {
            List<Message> messages = messageService.getMessagesBetween(user1, user2);
            logger.info("Fetched {} messages", messages.size());
            return ResponseEntity.ok(messages);
        } catch (Exception e) {
            logger.error("Error fetching messages: {}", e.getMessage(), e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }
}
