package com.chatapp.service;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.chatapp.model.Message;
import com.chatapp.repository.MessageRepository;

@Service
public class MessageService {

    private static final Logger logger = LoggerFactory.getLogger(MessageService.class);

    @Autowired
    private MessageRepository messageRepository;

    @Autowired
    private KafkaProducer kafkaProducer;
    
    public void sendMessage(Message message) {
        try {
            kafkaProducer.sendMessage(message);
            messageRepository.save(message);
            logger.info("✅ Message from '{}' to '{}' saved successfully", 
                        message.getSender(), message.getReceiver());
        } catch (Exception e) {
            logger.error("❌ Error saving message: {}", e.getMessage(), e);
            throw new RuntimeException("Failed to send message, please try again.");
        }
    }

    public List<Message> getMessagesBetween(String user1, String user2) {
        try {
            List<Message> list1 = messageRepository.findBySenderAndReceiver(user1, user2);
            List<Message> list2 = messageRepository.findBySenderAndReceiver(user2, user1);
        
            List<Message> allMessages = new ArrayList<>();
            allMessages.addAll(list1);
            allMessages.addAll(list2);
        
            allMessages.sort(Comparator.comparingLong(Message::getTimestamp));

            logger.info("✅ Retrieved {} messages between '{}' and '{}'", allMessages.size(), user1, user2);
            return allMessages;
        } catch (Exception e) {
            logger.error("❌ Error retrieving messages: {}", e.getMessage(), e);
            throw new RuntimeException("Could not fetch messages, please try again.");
        }
    }
}
