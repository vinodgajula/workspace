package com.chatapp.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
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
    public String sendMessage(@RequestBody Message message) {
        logger.info("Sending message from '{}' to '{}'", message.getSender(), message.getReceiver());
        messageService.sendMessage(message);
        logger.info("Message sent successfully");
        return "Message Sent!";
    }

    @GetMapping("/messages")
    public List<Message> getMessages(
            @RequestParam String user1,
            @RequestParam String user2) {
        logger.info("Fetching messages between '{}' and '{}'", user1, user2);
        List<Message> messages = messageService.getMessagesBetween(user1, user2);
        logger.info("Fetched {} messages", messages.size());
        return messages;
    }
}
